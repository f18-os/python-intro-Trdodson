# Lab 1: Word Counter

## Introduction

This is a simple word counting program. The program takes two text file names
- one being the file to be counted, the other being the output of the count -
counts the words, and then outputs a text file containing each word used in the file and the number of times they are used.

This directory contains:
 * The counting program, wordCount.py.
 * A program to test the accuracy of wordCount.py.
 * Text files, including "keys" for the program to read.

## How To Use

The program is executed from the command line. The user specifies the file
they want to count for and the desired name of the consequent output
file. Start the program using the following input:

~~~
$ python wordCount.py <input file> <output file>

~~~
Test the accuracy of the program using wordCountTest.py. This program takes
the file to be counted, the already generated output file, and one of the
"key" files, all of which already contain the correct output for the provided
text files.

~~~
$ python wordCountTest.py <input file><output file><solution key file>

~~~

## Refrences

This assignment was prepared in a manner consistent with the instructor's
requirements. All significant collaboration or guidance from external sources is clearly documented. These include:

https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python
- For understanding of syntax for splitting a line into single words in Python.

 https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
 - For understanding syntax for locating items in dictionaries in Python.

https://www.guru99.com/reading-and-writing-files-in-python.html for
understanding write() - For understanding implementation of read() and write().

https://www.geeksforgeeks.org/sorted-function-python/ - For understanding the
sorted() function.

https://docs.python.org/3/tutorial/datastructures.html#looping-techniques -
For iterating through a dictionary.

File checks, imports, "with open(...)" syntax, and implemtation of function arguments refrenced from wordCountTest.py, as provided by the instructor.

## Original Lab Instructions

This repository contains the code for the python introduction lab. The
purpose is to have a fairly simple python assignment that introduces
the basic features and tools of python

In the repository are two plain text files with lots of words. Your
assignment is to create a python 2 program which:
* takes as input the name of an input file and output file
* example

`$ python wordCount.py input.txt output.txt`
* keeps track of the total the number of times each word occurs in the text file 
* excluding white space and punctuation
* is case-insensitive
* print out to the output file (overwriting if it exists) the list of
  words sorted in descending order with their respective totals
  separated by a space, one word per line

To test your program we provide wordCountTest.py and two key
files. This test program takes your output file and notes any
differences with the key file. An example use is:

`$ python wordCountTest.py declaration.txt myOutput.txt declarationKey.txt`

The re regular expression library and python dictionaries should be
used in your program. 

Note that there are two major dialects of Python.  Python 3.0 is
incompatible with 2.7.   As a result, Python 2.7 remains popular.  All
of our examples are in 2.7.  We (mildly) encourage students to use 2.7
for their assignments. 
