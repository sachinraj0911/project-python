import PyPDF2

pdfFileObj = open('AddressProof2.pdf', 'rb')
b = open('example.pdf', 'wb+')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfWriter = PyPDF2.PdfFileWriter()

pageObj = pdfReader.getPage(0)
pdfWriter.addPage(pageObj)
pdfWriter.write(b)

pdfFileObj.close()
b.close()