#! /usr/bin/env python3

# Implementation of a basic shell. The program takes
# prompts from the user and runs other specified programs.
# This assignment was prepared in a manner consistent with
# the instructor's requirements. All significant collaboration
# or guidance from external sources is clearly documented. See
# README.md for detailed instructions and refrences.

import os, sys, time, re

while(True): # Keep asking for prompts 'till user types "exit"

    pid = os.getpid()
    args = input("Command>") # Prompt user for a command.
    type(args)

    if(args.lower() == "exit"):      # If you see exit command, break the loop (kill the shell)
        break

    args = args.split() # Parse the command for arguments
    rc = os.fork()      # Create a child process.

    # Handling the fork. Heavily based on p3-execv.py and p4-redirect.py. See README.
    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)
        
    elif rc == 0:       # This is a child.
        if '>' in args: # Redirect detected. The user wants to redirect the output.
            os.close(1)
            sys.stdout = open(args[args.index('>') + 1], "w")   # Redirect output of program to specified text file.
            fd = sys.stdout.fileno()                     # define file descriptor
            os.set_inheritable(fd,True)                  # Set fd as inheritable
            args.remove(args[args.index('>') + 1])       # Remove the redirect file from args
            args.remove('>')                             # Remove the redirect char

        for dir in re.split(":", os.environ['PATH']):    # Try each directory.
            program = "%s/%s" % (dir, args[0])           # Path to program is here
            try:
                os.execve(program, args, os.environ)     # Try to run the program.
            except FileNotFoundError:
                pass
            
        os.write(2, ("Child: Could not exec %s \n" % program).encode())
        sys.exit(1)
        
    else:                        # If rc isn't 0, this is a parent.
        childPidCode = os.wait() # Wait for the child to die.
