#!y /usr/bin/env python3

#A simple word counter. Takes two file names as input, reads one, and then writes all words with their counts to second file.
#This assignment was prepared in a manner consistent with the instructor's requirements. All significant collaboration or guidance from external sources is clearly documented; see Readme for details.

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

# set input and output files and check if input is valid. Code modified from wordCountTest.py.
if len(sys.argv) is not 3:
    print("Erroneous input. Correct usage: wordCount.py <input file> <output file> ")
    exit()

inputName = sys.argv[1]  # Save name of input file.
outputName = sys.argv[2] # Save name of output file
words = {}               # Words and counts will be stored here.


# Make sure the input file exists! Modified from wordCountTest.py.
if not os.path.exists(inputName):
    print ("Text file %s doesn't exist! Exiting..." % inputName)
    exit()


# Opens file and counts the words! Modified from wordCountTest.py and stack overflow.
# Refrenced https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python
# Refrenced https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary

with open(inputName, 'r') as myFile:
    for line in myFile:                          # For every line in the file:
        line = line.strip()                      # Delete newline chars.
        for w in re.split("['\s\t.,-;:]", line): # For every word in the line (split at spaces & punctuation):
            if w.lower() == "":                  #Don't count whitespace. lower() for case insenstivity.
                continue
            if w.lower() in words:
                words[w.lower()] += 1
            else:
                words[w.lower()] = 1
                
# Write to the output file.
# Refrenced https://www.guru99.com/reading-and-writing-files-in-python.html for understanding write()
# Refrenced https://www.geeksforgeeks.org/sorted-function-python/
# Refrenced https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

f = open(outputName,"w+")
for w, n in sorted(words.items()):
    f.write(w + " " + str(n) + "\n")

f.close()
