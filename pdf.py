import fitz  # PyMuPDF

A4_HEIGHT = 842  # points (11.69 inches)
A4_WIDTH = 595   # points (8.27 inches)

doc = fitz.open("doji.pdf")
new_doc = fitz.open()

for page in doc:
    rect = page.rect
    y0 = 0
    while y0 < rect.height:
        y1 = min(y0 + A4_HEIGHT, rect.height)
        clip = fitz.Rect(0, y0, A4_WIDTH, y1)
        new_page = new_doc.new_page(width=A4_WIDTH, height=y1 - y0)
        new_page.show_pdf_page(new_page.rect, doc, page.number, clip=clip)
        y0 = y1

new_doc.save("doji_split.pdf")
