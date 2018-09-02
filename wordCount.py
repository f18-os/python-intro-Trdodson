#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools

# set input and output files - code modified from wordCountTest.py.
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file> ")
    exit()

inputName = sys.argv[1]
outputName = sys.argv[2]

#Create outpuutfile.
f= open(outputName,"w+")

f.close()
