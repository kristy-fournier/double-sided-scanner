import pypdf
global pdfWriter

def flip(pdfObj:pypdf.PdfReader) -> pypdf.PdfWriter:

    pdfWriter = pypdf.PdfWriter()
    pdfReader = pypdf.PdfReader(pdfObj)

    pdfLen = len(pdfReader.pages)

    for i in range(pdfLen):
        pdfWriter.add_page(pdfReader.pages[pdfLen-i-1])
    return pdfWriter

if __name__ == "__main__":
    pdfName=input("Enter PDF Name: ")
    if pdfName == "":
        pdfName = "evens.pdf"
    pdfObj=open(pdfName,'rb')
    pdfWriter = flip(pdfObj)
    pdfWriter.write("evens-flipped.pdf")