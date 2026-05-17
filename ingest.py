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

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    """
    Splits a long string into overlapping chunks of fixed size.
    
    chunk_size: number of characters per chunk
    overlap: how many characters to repeat between consecutive chunks
     
    """
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        
        if chunk.strip():
            chunks.append(chunk)
            
        start += chunk_size - overlap
    return chunks

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 ingest.py <path_to_pdf>")
        
    else:
        pdf_path = sys.argv[1]
        
        # Extract
        text = extract_text_from_pdf(pdf_path)
        print(f"Total characters extracted: {len(text)}")
        
        # Chunk
        chunks = chunk_text(text)
        print(f"Total chunks created: {len(chunks)}")
        print(f"\n--- Preview of chunk 1 ---\n{chunks[0]}")
        print(f"\n--- Preview of chunk 2 ---\n{chunks[1]}")