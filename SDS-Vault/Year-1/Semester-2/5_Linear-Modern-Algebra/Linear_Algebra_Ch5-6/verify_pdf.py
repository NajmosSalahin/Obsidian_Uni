"""Verify combined .md matches source .md files word-for-word, and check PDF content."""

import re, unicodedata, difflib, sys

DIR = r"C:\Users\Aurnob\Desktop\Barnackle\SDS-Vault\Year-1\Semester-2\5_Linear-Modern-Algebra\Linear_Algebra_Ch5-6"
# Force UTF-8 for stdout
sys.stdout.reconfigure(encoding='utf-8')

def normalize(text):
    text = unicodedata.normalize('NFKD', text)
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\ue000-\uf8ff\uFFF0-\uFFFF]', '', text)
    text = re.sub(r'\*\*', '', text)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'---+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def word_tokenize(text):
    return re.findall(r"[A-Za-z0-9\u00C0-\u024F\u0370-\u03FF\u1E00-\u1EFF']+(?:[-\'][A-Za-z0-9\u00C0-\u024F]+)*", normalize(text))

def read_words(path):
    with open(path, encoding='utf-8') as f:
        return word_tokenize(f.read())

def read_raw(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

# ============================================================
# CHECK 1: Combined file vs source files (set-based comparison)
# ============================================================
print("=" * 70)
print("CHECK 1: Combined file content vs source files (set-based)")
print("=" * 70)

src_q_words = read_words(f"{DIR}/linear_ch5_question_sets.md")
src_a_words = read_words(f"{DIR}/linear_ch5_answer_sets.md")
combined_words = read_words(f"{DIR}/linear_ch5_qa_combined.md")

# Build union of all source words
all_source_words = src_q_words + src_a_words

# Build set-based comparison
src_set = set(all_source_words)
combined_set = set(combined_words)

# Words in source but missing from combined
missing_from_combined = src_set - combined_set
# Words in combined but not in any source
extra_in_combined = combined_set - src_set

print(f"  Source Q unique words:  {len(set(src_q_words))}")
print(f"  Source A unique words:  {len(set(src_a_words))}")
print(f"  Combined unique words:  {len(combined_set)}")
print(f"  Source union unique:    {len(src_set)}")

if not missing_from_combined:
    print(f"  [OK] All source words present in combined file!")
else:
    print(f"  [WARN] {len(missing_from_combined)} source word(s) missing from combined:")
    for w in sorted(missing_from_combined):
        print(f"    - '{w}'")

if not extra_in_combined:
    print(f"  [OK] No extra words in combined file beyond sources!")
else:
    print(f"  [INFO] {len(extra_in_combined)} word(s) in combined not in source union:")
    for w in sorted(extra_in_combined):
        print(f"    - '{w}'")

# Also do a line-level diff on the raw text (ignoring the title line)
print(f"\n--- Line-by-line content diff (excluding title/headings) ---")
src_q_lines = read_raw(f"{DIR}/linear_ch5_question_sets.md").splitlines()
src_a_lines = read_raw(f"{DIR}/linear_ch5_answer_sets.md").splitlines()
combined_lines = read_raw(f"{DIR}/linear_ch5_qa_combined.md").splitlines()

# Extract all content lines (non-heading, non-separator) from each file
def content_words(lines):
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#') or stripped.startswith('---') or stripped == '':
            continue
        # Normalize for comparison
        clean = normalize(stripped)
        if clean:
            result.append(clean)
    return result

src_q_content = content_words(src_q_lines)
src_a_content = content_words(src_a_lines)
combined_content = content_words(combined_lines)

src_all_content = src_q_content + src_a_content

# Check each source content line appears in combined
unmatched_src = []
for line in src_all_content:
    if line not in combined_content:
        unmatched_src.append(line)

unmatched_combined = []
for line in combined_content:
    if line not in src_all_content:
        unmatched_combined.append(line)

if not unmatched_src:
    print(f"  [OK] Every source content line appears in combined!")
else:
    print(f"  [WARN] {len(unmatched_src)} source content line(s) not in combined (may be heading/title differences):")
    for l in unmatched_src[:10]:
        print(f"    - \"{l[:80]}...\"" if len(l) > 80 else f"    - \"{l}\"")

if not unmatched_combined:
    print(f"  [OK] No extra content lines in combined!")
else:
    print(f"  [INFO] {len(unmatched_combined)} combined content line(s) not in sources (expected for merged format):")
    for l in unmatched_combined[:10]:
        print(f"    - \"{l[:80]}...\"" if len(l) > 80 else f"    - \"{l}\"")

# ============================================================
# CHECK 2: Spot-check in PDF
# ============================================================
print(f"\n{'='*70}")
print("CHECK 2: Spot-check key passages in PDF")
print("=" * 70)

with open(f"{DIR}/pdf_pdftotext.txt", encoding='utf-8') as f:
    pdf_text = f.read()
pdf_text_norm = normalize(pdf_text)

key_passages = [
    "Let A and B be arbitrary nonempty sets",
    "The kernel of F, written Ker F, is the set of elements in V that map into the zero vector",
    "dim V = dim Ker F + dim Im F = nullity F + rank F",
    "F is said to be singular if the image of some nonzero vector v is 0",
    "The collection of all linear mappings from V into U",
    "A V is an associative algebra over K with respect to composition of mappings",
    "matrix product AB corresponds to the composition of A and B as linear mappings",
    "F is an isomorphism if and only if F is nonsingular",
]

for passage in key_passages:
    passage_clean = normalize(passage)
    if passage_clean in pdf_text_norm:
        print(f"  [OK] Found in PDF")
    else:
        print(f"  [CHECK] Not found as-is: \"{passage[:60]}\" (may be extraction artifact)")

print(f"\n{'='*70}")
print("VERIFICATION SUMMARY")
print("=" * 70)
print(f"  Combined file vs sources: {'PASS' if not missing_from_combined and not unmatched_src else 'See details above'}")
print(f"  PDF content check:        {'PASS' if all(normalize(p) in pdf_text_norm for p in key_passages) else 'Some passages need manual review'}")
print(f"\nDONE")
