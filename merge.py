#!/usr/bin/env python

from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

input1 = open("rd.pdf", "rb")
input2 = open("document2.pdf", "rb")

# add the first 3 pages of input1 document to output
merger.append(fileobj = input1, pages = (0,1))

# append entire input3 document to the end of the output document
merger.append(input2)

merger.append(fileobj = input1, pages = (0,1))

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)
