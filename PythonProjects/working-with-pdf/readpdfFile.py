import PyPDF2

pdfFileObj = open('AddressProof2.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

totalPageObj = pdfReader.getNumPages()

pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

pdfFileObj.close()