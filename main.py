import sys
from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import RectangleObject

if len(sys.argv) !=  2:
    print("Invalid command line argument.")
    sys.exit("USAGE: main.py <file.pdf>")

reader = PdfReader(sys.argv[1])
writer = PdfWriter()

targetPage = reader.pages[3]

targetPage.cropbox = RectangleObject((40, 120, 620, 620))

writer.add_page(targetPage)

with open(f"out.pdf", "wb") as fp:
    writer.write(fp)