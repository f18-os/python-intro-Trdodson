#! /usr/bin/env python3

#Implementation for a basic shell. Code base provided by instructor. See README for details.y

import os, sys, time, re

while(True): # Keep asking for prompts 'till user types "exit"

    pid = os.getpid()
    args = input("Command>") # Prompt user for a command.
    type(args)

    if(args == "exit"): # If you see exit command, break the loop (kill the shell)
        break

    args = args.split() # Parse the command for arguments
    
    os.write(1, ("About to fork (pid:%d)\n" % pid).encode())
    rc = os.fork()

    # Handling the fork. Heavily based on p3-execv.py and p4-redirect.py. See README.
    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)
    elif rc == 0:
    
        os.write(1, ("I am child.  My pid==%d.  Parent's pid=%d\n" % (os.getpid(), pid)).encode())
        os.close(1)
        sys.stdout = open("shell-output.txt", "w")   # Redirect output of program to text file.
        fd = sys.stdout.fileno()                     # define file descriptor
        os.set_inheritable(fd,True)                  # Set fd as inheritable
        os.write(2,("Child: opened fd=%fd for writing\n" % fd).encode())

        for dir in re.split(":", os.environ['PATH']):    # try each directory.
            program = "%s/%s" % (dir, userCmd[0])        # path to program is here
            try:
                os.execve(program, userCmd, os.environ)  # Try to run the program.
            except FileNotFoundError:
                pass
            
        os.write(2, ("Child: Could not exec %s \n" % program).encode())
        sys.exit(1)
        
    else:
        os.write(1, ("I am parent.  My pid=%d.  Child's pid=%d\n" % (pid, rc)).encode())
        childPidCode = os.wait() #Wait for child to die
        os.write(1, ("Parent: Child %d terminated with exit code %d\n" % childPidCode).encode())
