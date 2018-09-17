# Lab 2 - Basic Shell

This directory contains a basic shell program. It takes commands from the
user, forks a child process, and runs the program specified.

## How To Use
This shell, when executed, will immeadiately prompt the user for a command.
Enter any Bash command when prompted.

A few to try:

~~~
wc shell.py
~~~

~~~
ls
~~~

~~~
which ls
~~~

~~~
cat README.md
~~~

If you wish to redirect the output to a specific file, use the '>'
character. For example, to write the output of wc shell.py to
output.txt, simply enter the following when prompted:
~~~
wc shell.py > output.txt
~~~
It will create and write to the file if it does not already exist -
otherwise, it will simply overwrite the existing file. It is also possible
to redirect input using '<' and to append an existing output using
'>>'.

To exit the shell, simply type "exit" into the prompt.

## Refrences

This assignment was prepared in a manner consistent with the instructor's
requirements. All significant collaboration or guidance from external sources
is clearly documented. These include:

* p3-execv.py and p4-redirect.py; the shell seen here was built based on the
  structure of these demo programs provided by the instructor. Namely, the
  basic structure of the forked 'if-else' branches for parent and child
  processes and some of the structure of the 'execv' block in the
  child(args) method.
  
Further edits as warranted.
