#! /usr/bin/env python3

#Implementation for a basic shell. Code base provided by instructor. See README for details.

import os, sys, time, re

pid = os.getpid()

userCmd = input("Insert command to run on shell.py:")
type(userCmd)
    
os.write(1, ("About to fork (pid:%d)\n" % pid).encode())

rc = os.fork()

if rc < 0:
    os.write(2, ("fork failed, returning %d\n" % rc).encode())
    sys.exit(1)

elif rc == 0:
    os.write(1, ("I am child.  My pid==%d.  Parent's pid=%d\n" % (os.getpid(), pid)).encode())
    args = [userCmd, "shell.py"]

    os.close(1)
    sys.stdout = open("shell-output.txt", "w")
    fd = sys.stdout.fileno()
    os.set_inheritable(fd,True)
    os.write(2,("Child: opened %fd for writing\n" % fd).encode())
    
    for dir in re.split(":", os.environ['PATH']): # try each directory.
        program = "%s/%s" % (dir, args[0])        # path to program is here
        try:
            os.execve(program, args, os.environ) #Execute the program
        except FileNotFoundError:
            pass
    os.write(2, ("Child: Could not exec %s \n" % program).encode())
    sys.exit(1)
else:
    os.write(1, ("I am parent.  My pid=%d.  Child's pid=%d\n" % (pid, rc)).encode())
    childPidCode = os.wait() #Wait for child to die
    os.write(1, ("Parent: Child %d terminated with exit code %d\n" % childPidCode).encode())
