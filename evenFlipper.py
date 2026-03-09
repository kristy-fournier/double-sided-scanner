import pypdf
global pdfWriter

# Invert the order of pages in a pdfReader
def flip(pdfReader:pypdf.PdfReader) -> pypdf.PdfWriter:

    pdfWriter = pypdf.PdfWriter()

    pdfLen = len(pdfReader.pages)

    for i in range(pdfLen):
        pdfWriter.add_page(pdfReader.pages[pdfLen-i-1])
    return pdfWriter

if __name__ == "__main__":
    pdfName=input("Enter PDF Name: ")
    if pdfName == "":
        pdfName = "evens.pdf"
    pdfObj=open(pdfName,'rb')
    pdfReader = pypdf.PdfReader(pdfObj)
    pdfWriter = flip(pdfObj)
    pdfWriter.write("evens-flipped.pdf")