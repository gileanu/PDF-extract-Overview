from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import RectangleObject

reader = PdfReader("test1.pdf")
writer = PdfWriter()

targetPage = reader.pages[3]

targetPage.cropbox = RectangleObject((40, 120, 620, 620))

writer.add_page(targetPage)

with open(f"out.pdf", "wb") as fp:
    writer.write(fp)