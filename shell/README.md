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

It will create and write to the file if it does not already exist - otherwise,
it will simply overwrite the existing file. It is also possible to redirect
input using '<' and to append an existing output using '>>'.

Piping is only partially implemented: if '|' is found in the input, the child
will fork another child, which will write a greeting message to the pipe. Its
parent will read it and print it out.

To change the current working directory, use cd (e.g. cd ..). To exit the
shell, simply type "exit" into the prompt.

## Refrences

This assignment was prepared in a manner consistent with the instructor's
requirements. All significant collaboration or guidance from external sources
is clearly documented. These include:

* p3-execv.py and p4-redirect.py; the shell seen here was built based on the
  structure of these demo programs provided by the instructor. Namely, the
  basic structure of the forked 'if-else' branches for parent and child
  processes and some of the structure of the 'execv' block in the
  child(args) method.

* p5-pipe-fork: this was heavily refrenced for the childPipe() method and the
 child() method. Specifically, when a pipe is detected in the child: piping pr
 and pw and redirecting to the pipe is understood, but they have not yet been
 modified to run programs using the pipe's contents.
  
Further edits as warranted.
