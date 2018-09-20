# Collaborators

* p3-execv.py and p4-redirect.py; the shell seen here was built based on the
structure of these demo programs provided by the instructor.

* Namely, the basic structure of the forked 'if-else' branches, functions for
redirection (redirect.py) for parent and child processes and some of the
structure of the 'execv' block in the child(args) method (p4-exec.py).

* p5-pipe-fork.py was heavily refrenced for the childPipe() method and the
 child() method. Specifically, when a pipe is detected in the child: creating
 the pipe and redirecting to the pipe is understood, but they have not yet
 been modified to run programs using the pipe's contents.
