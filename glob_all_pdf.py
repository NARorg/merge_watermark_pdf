#!/usr/bin/env python

import sys
import glob
import os


for file in glob.iglob('/Users/rgc/Rocket/rd_old/*/*pdf'):
  newFile = file.replace('rd_old', 'rd')
  #print file, newFile
  os.popen('./watermark_and_add_end.py "' + file + '" "' + newFile + '"') 
  #print file + 'done!'
