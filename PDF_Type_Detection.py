import pdfplumber

def is_text_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            print(text)
            if text:
                return True
            
    return False

is_text = is_text_pdf(r"D:\Freelance_projects\PDF-to-Excel-Converter-with-High-Accuracy-using-Python\Cloud engineer.pdf")
print(is_text)