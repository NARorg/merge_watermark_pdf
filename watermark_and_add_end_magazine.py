#!/usr/bin/env python

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

output = PdfFileWriter()
input = PdfFileReader(open(sys.argv[1], "rb"), strict=False)
watermark = PdfFileReader(open("./rdfootermag.pdf", "rb"))
lastPage = PdfFileReader(open("./mag.pdf", "rb"))

# print how many pages input1 has:
#print("test.pdf has %d pages." % input.getNumPages())
#print("watermark.pdf has %d pages." % watermark.getNumPages())

for pageNum in xrange(input.getNumPages()):
  page = input.getPage(pageNum)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

output.addPage(lastPage.getPage(0))

outputStream = open(sys.argv[2], "wb")
print sys.argv[2]
output.write(outputStream)
outputStream.close()
