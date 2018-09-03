#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools

# set input and output files and check if input is valid km- code modified from wordCountTest.py.
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file> ")
    exit()

inputName = sys.argv[1]
outputName = sys.argv[2]
words = {}

#Opens file and counts the words! Modified from wordCountTest.py and stack overflow.
#(See https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python)
with open(inputName, 'r') as myFile:
    for line in myFile:
        line = line.strip()
        for w in re.split('[ \t.,-:;]', line):
            if w.lower() in words:
                words[w] += 1
            else:
                words[w] = 1
                
#Write to output file. Refrenced https://www.guru99.com/reading-and-writing-files-in-python.html
f = open(outputName,"w+")
for w, n in sorted(words.items()):
    f.write(w + " " + str(n) + "\n")

f.close()
