import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import io
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pdf_path = r"C:\Users\Aurnob\Desktop\Barnackle\SDS-Vault\Year-1\Semester-2\3_Calculus-I\03_My-Notes\Lecture note_Calculus I(6)(2)-1.pdf"
output_dir = r"C:\Users\Aurnob\Desktop\Barnackle\SDS-Vault\Year-1\Semester-2\3_Calculus-I"

doc = fitz.open(pdf_path)
all_text = []

for page_num in range(doc.page_count):
    page = doc[page_num]
    pix = page.get_pixmap(dpi=300)
    img_data = pix.tobytes("png")
    img = Image.open(io.BytesIO(img_data))
    
    text = pytesseract.image_to_string(img, lang='eng')
    all_text.append(f"--- Page {page_num + 1} ---\n{text}")
    print(f"Page {page_num + 1}/{doc.page_count} done")

full_text = "\n\n".join(all_text)
output_path = os.path.join(output_dir, "ocr_output.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"\nOCR complete. Output saved to {output_path}")
print(f"Total characters: {len(full_text)}")
