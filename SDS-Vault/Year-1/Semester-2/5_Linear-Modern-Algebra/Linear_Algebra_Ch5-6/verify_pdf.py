import re
import difflib
from pypdf import PdfReader

DIR = r"C:\Users\Aurnob\Desktop\Barnackle\SDS-Vault\Year-1\Semester-2\5_Linear-Modern-Algebra\Linear_Algebra_Ch5-6"

def extract_pdf_words(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + "\n"
    return tokenize(text)

def read_md_words(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    # Strip markdown formatting
    text = re.sub(r'\*\*', '', text)  # bold markers
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)  # headings
    text = re.sub(r'---+', '', text)  # horizontal rules
    return tokenize(text)

def tokenize(text):
    """Extract clean word tokens, preserving order."""
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Split into words (sequences of word chars, allow intra-word hyphens/apostrophes)
    words = re.findall(r"[A-Za-z0-9\u00C0-\u024F\u0370-\u03FF\u1E00-\u1EFF']+(?:[-\'][A-Za-z0-9\u00C0-\u024F]+)*", text)
    return words

def verify_file(label, md_path, pdf_words):
    md_words = read_md_words(md_path)
    
    matcher = difflib.SequenceMatcher(None, pdf_words, md_words)
    differences = []
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            continue
        pdf_seg = pdf_words[i1:i2]
        md_seg = md_words[j1:j2]
        if tag == 'replace':
            differences.append(f"  REPLACE: PDF has [{', '.join(pdf_seg[:10])}{'...' if len(pdf_seg)>10 else ''}] but MD has [{', '.join(md_seg[:10])}{'...' if len(md_seg)>10 else ''}]")
        elif tag == 'delete':
            differences.append(f"  DELETE (in PDF, missing from MD): [{', '.join(pdf_seg[:10])}{'...' if len(pdf_seg)>10 else ''}]")
        elif tag == 'insert':
            differences.append(f"  INSERT (extra in MD, not in PDF): [{', '.join(md_seg[:10])}{'...' if len(md_seg)>10 else ''}]")
    
    total_words_pdf = len(pdf_words)
    total_words_md = len(md_words)
    match_ratio = matcher.ratio()
    
    print(f"\n{'='*70}")
    print(f"FILE: {label}")
    print(f"{'='*70}")
    print(f"  PDF word count (approx): {total_words_pdf}")
    print(f"  MD  word count:           {total_words_md}")
    print(f"  Match ratio:              {match_ratio:.4f}")
    
    if not differences:
        print(f"  ✅ No content differences found — word-for-word match!")
    else:
        print(f"  ⚠️  {len(differences)} difference(s) found:")
        for d in differences:
            print(d)

print("Extracting PDF text...")
pdf_words = extract_pdf_words(f"{DIR}/Linear.pdf")
print(f"PDF: {len(pdf_words)} word tokens extracted")

# Check each .md file
verify_file("linear_ch5_question_sets.md", f"{DIR}/linear_ch5_question_sets.md", pdf_words)
verify_file("linear_ch5_answer_sets.md", f"{DIR}/linear_ch5_answer_sets.md", pdf_words)
verify_file("linear_ch5_qa_combined.md", f"{DIR}/linear_ch5_qa_combined.md", pdf_words)

print(f"\n{'='*70}")
print("DONE")
