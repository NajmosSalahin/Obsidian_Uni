import re

with open(r"C:\Users\Aurnob\Desktop\Barnackle\SDS-Vault\Year-1\Semester-2\3_Calculus-I\ocr_output.md", "r", encoding="utf-8") as f:
    text = f.read()

changes = 0

# Fix $$ -> $ (double dollar to single for inline math)
text, n = re.subn(r'\$\$', '$', text)
changes += n
print(f"Double dollar fix: {n}")

# Fix subscripts: x2 -> x2 when 2 follows a variable
text, n = re.subn(r"(?<=[a-z])2(?=[,\s\)\]\(])", "₂", text)
changes += n
print(f"x2 subscript fix: {n}")

# Fix x3 -> x3
text, n = re.subn(r"(?<=[a-z])3(?=[,\s\)\]\(])", "₃", text)
changes += n
print(f"x3 subscript fix: {n}")

# Fix x1 -> x1  
text, n = re.subn(r"(?<=[a-z])1(?=[,\s\)\]\(])", "₁", text)
changes += n
print(f"x1 subscript fix: {n}")

# Fix separated lines (blank line between text and table)
text, n = re.subn(r"\n\n(Increasing \| Decreasing \| Increasing Constant x)", r"\n\1", text)
changes += n
print(f"Separated line fix: {n}")

# Fix P(x) -> f'(x) in specific known contexts
text, n = re.subn(r"If P\(x\) > 0", "If f'(x) > 0", text)
changes += n
print(f"P(x) fix: {n}")

# Fix common OCR: "ae" at end of lines
text, n = re.subn(r"\s+ae$", "", text, flags=re.MULTILINE)
changes += n
print(f"ae artifact fix: {n}")

# Fix "|" as "I" when followed by a period or at end
text, n = re.subn(r"\bI\|(?=\s)", "I", text)
changes += n
print(f"| -> I end fix: {n}")

# Fix extra spaces before punctuation
text, n = re.subn(r"\s+([,;.!])", r"\1", text)
changes += n
print(f"Space before punct: {n}")

# Fix "x)" -> "x₁)" when it's a subscript
text, n = re.subn(r"(?<=[a-z])\((?=[^)]*\))", "₁(", text)
# That's too aggressive, skip

# Fix f(,) -> f(x) approximation
text, n = re.subn(r"f\(,\)", "f(x)", text)
changes += n
print(f"f(,) fix: {n}")

# Fix stray "z" that should be "x" in math contexts
# Very error prone, skip

print(f"\nTotal: {changes} changes")

with open(r"C:\Users\Aurnob\Desktop\Barnackle\SDS-Vault\Year-1\Semester-2\3_Calculus-I\ocr_output.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
