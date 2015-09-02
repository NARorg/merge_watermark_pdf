#!/usr/bin/env python

from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input = PdfFileReader(open("document2.pdf", "rb"))
watermark = PdfFileReader(open("rdfooter.pdf", "rb"))

# print how many pages input1 has:
print("test.pdf has %d pages." % input.getNumPages())
print("watermark.pdf has %d pages." % watermark.getNumPages())

# add page 0 from input, but first add a watermark from another PDF:
page = input.getPage(0)
page.mergePage(watermark.getPage(0))
output.addPage(page)

# finally, write "output" to document-output.pdf
outputStream = file("outputs.pdf", "wb")
output.write(outputStream)
outputStream.close()
