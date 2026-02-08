import pypdf
import evenFlipper
global pdfWriter

#pdf1name = input("Name of pdf1? ")
#pdf2name = input("Name of pdf2? ")
pdf1name = "odds.pdf"
pdf2name = "evens.pdf"

pdf1obj = open(pdf1name, 'rb')
pdf2obj = open(pdf2name, 'rb')

pdfWriter= pypdf.PdfWriter()

pdfReader1 = pypdf.PdfReader(pdf1obj)
pdfReader2 = pypdf.PdfReader(pdf2obj)

pdfLen1 = len(pdfReader1.pages)
pdfLen2 = len(pdfReader2.pages)

totalLen = pdfLen1 + pdfLen2

for i in range(totalLen):
    try:
        pdfWriter.add_page(pdfReader1.pages[i])
    except:
        pass
    try:
        pdfWriter.add_page(pdfReader2.pages[i])
    except:
        pass

pdfWriter.write("final.pdf")