#!/usr/bin/env python

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

output = PdfFileWriter()
input = PdfFileReader(open(sys.argv[1], "rb"), strict=False)
lastPage = PdfFileReader(open("./mag.pdf", "rb"))

# print how many pages input1 has:
#print("test.pdf has %d pages." % input.getNumPages())

for pageNum in xrange(input.getNumPages()):
  page = input.getPage(pageNum)
  output.addPage(page)

output.addPage(lastPage.getPage(0))

outputStream = open(sys.argv[2], "wb")
print sys.argv[2]
output.write(outputStream)
outputStream.close()
