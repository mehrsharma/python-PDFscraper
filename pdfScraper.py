import PyPDF2 as p2;

#feel free to replace the file in the double quotes
PDFfile = open("samplePDF.pdf", "rb")

pdfread = p2.PdfFileReader(PDFfile)

#if your file is only one page, uncomment lines 9&10, and remove lines 14-18
#x = pdfread.getPage(0)
#print(x.extractText())


# modify range and starting q value as needed
q = 0   #this starts reading the file at page 0, or the first page
for q in range (0,0):   #samplePDF is 4 pages long and starts on page 0, so the range is 0 to 3 pages
    x = pdfread.getPage(q)
    print(x.extractText())
    q += 1
