import re

with open(r"C:\Users\Aurnob\Desktop\Barnackle\SDS-Vault\Year-1\Semester-2\3_Calculus-I\ocr_output.md", "r", encoding="utf-8") as f:
    text = f.read()

changes = 0

# === Fix remaining common OCR issues ===

# 1. "fis" -> "f is" (common OCR join)
text, n = re.subn(r'\bfis\b', 'f is', text)
changes += n
print(f"fis fix: {n}")

# 2. "Ler" -> "Let" (common)
text, n = re.subn(r'\bLer\b', 'Let', text)
changes += n
print(f"Ler fix: {n}")

# 3. "_/f" -> "f" at start of list items
text, n = re.subn(r'_/f\b', 'f', text)
changes += n
print(f"_/f fix: {n}")

# 4. "/f" -> "f" at start of lines  
text, n = re.subn(r'^/f\b', 'f', text, flags=re.MULTILINE)
changes += n
print(f"/f fix: {n}")

# 5. "(ce)" -> "(c)" in theorem/definition labels
text, n = re.subn(r'\(ce\)', '(c)', text)
changes += n
print(f"(ce) fix: {n}")

# 6. "{a, b)" -> "[a, b)" etc (curly braces used as brackets)
text, n = re.subn(r'\{([a-zA-Z0-9,∞²³\s]+)\]', r'[\1]', text)
changes += n
print(f"{{ -> [ fix: {n}")

# 7. "|" used as "I" (capital i) in interval context
# This is tricky - only when | stands alone near interval notation
text, n = re.subn(r'\b\|(?=\s)', 'I', text)
changes += n
print(f"| -> I fix: {n}")

# 8. "P(x)" -> "f'(x)" in derivative context - very error prone, skip
# Instead fix specific known patterns

# 9. Remove stray figure artifacts (lines with mostly special chars)
def is_garbage_line(line):
    stripped = line.strip()
    if not stripped or len(stripped) < 3:
        return False
    # Lines that are mostly non-alphanumeric characters from figures
    alpha = sum(c.isalpha() for c in stripped)
    total = len(stripped)
    if total > 5 and alpha / total < 0.3:
        return True
    return False

lines = text.split('\n')
filtered = []
garbage_count = 0
for line in lines:
    # Keep page markers, headers, and blank lines
    if line.startswith('#') or line.startswith('---') or line.strip() == '':
        filtered.append(line)
    elif is_garbage_line(line):
        garbage_count += 1
        # Replace with empty line
        filtered.append('')
    else:
        filtered.append(line)

text = '\n'.join(filtered)
print(f"Garbage lines removed: {garbage_count}")
changes += garbage_count

# 10. Clean up blank lines again
text, n = re.subn(r'\n{4,}', '\n\n\n', text)
changes += n
print(f"Blank lines cleanup: {n}")

# 11. Fix "|" between words (like "Increasing | Decreasing | Increasing Constant x")
text, n = re.subn(r'(\w)\s*\|\s*(\w)', r'\1 | \2', text)
changes += n
print(f"Pipe spacing: {n}")

# 12. "F" used as "f" (capital at start of sentences about functions)
# Only fix when F is followed by '(x)' or '(x)'
text, n = re.subn(r'\bF\(([^)]+)\)', r'f(\1)', text)
changes += n
print(f"F( -> f(: {n}")

# 13. Fix "x;" -> "x₁" and similar subscript notation
# (OCR reads subscripts as x;)
text, n = re.subn(r'([a-zA-Z]);', r'\1₁', text)
changes += n
print(f"Subscript ; fix: {n}")

# 14. Fix "x2" -> "x₂" in math contexts (after intervals and math)
# Careful: only when x2 means x₂ not x×2
text, n = re.subn(r'(?<=\b[a-zA-Z])2(?=\s*[\),;]|\s+and|\s+in)', r'₂', text)
changes += n
print(f"Subscript 2 fix: {n}")

# 15. Fix "x3" -> "x₃" in math contexts
text, n = re.subn(r'(?<=\b[a-zA-Z])3(?=\s*[\),;]|\s+and|\s+in)', r'₃', text)
changes += n
print(f"Subscript 3 fix: {n}")

print(f"\nTotal additional changes: {changes}")

with open(r"C:\Users\Aurnob\Desktop\Barnackle\SDS-Vault\Year-1\Semester-2\3_Calculus-I\ocr_output.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Done.")
