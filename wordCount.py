#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools

# set input and output files - code modified from wordCountTest.py.
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file> ")
    exit()

inputName = sys.argv[1]
outputName = sys.argv[2]
count = 0

#Opens file and counts the words! Modified from wordCountTest.py.
with open(inputName, 'r') as myFile:
    for line in myFile:
        for w in line.split():
            count += 1
        

#Print number of lines and create outputfile.
print(count)
f= open(outputName,"w+")

f.close()
