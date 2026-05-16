import fitz

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Opens a PDF and extracts all text content page by page. Returns a single string with all the text.
    """
    doc = fitz.open(pdf_path)
    full_text = ""
    
    for page_num, page in enumerate(doc):
        text = page.get_text()
        full_text += f"\n--- Page {page_num + 1} ---\n{text}"
    
    doc.close()
    return full_text

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 ingest.py <path_to_pdf>")
    else:
        pdf_path = sys.argv[1]
        text = extract_text_from_pdf(pdf_path)
        print(text[:2000])
        print(f"\n Total characters extracted: {len(text)}")    