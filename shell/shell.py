#! /usr/bin/env python3

# Implementation of a basic shell. The program takes prompts from the user and
# runs other specified programs.  This assignment was prepared in a manner
# consistent with the instructor's requirements. All significant collaboration
# or guidance from external sources is clearly documented. See README.md for
# detailed instructions and refrences.

import os, sys, time, re, fileinput
        
def parent():
    while(True):                        # Keep asking for prompts 'till user types "exit"

        pid = os.getpid()
        prompt = os.environ["PS1"]

        if not prompt:                  # Check if PS1 is set.
            try:
                args = input("$ ")      # Prompt with a set string.
            except EOFError:            # Check for EOF.  
                sys.exit(1)
        else:
            try:
                args = input(prompt)    # Prompt with the PS1 variable.
            except EOFError:
                sys.exit(1)
        
        type(args)
        
        if(args.lower() == "exit"):      # If you see exit command, break the loop (kill the shell)
            sys.exit(1)
        elif (args == ""):
            continue
        
        args = args.split()              # Parse the command for arguments

        if 'cd' in args:                 # If cd command is used, change working directory.
            try:
                os.chdir(args[1])
            except FileNotFoundError:
                os.write(2,("Error: %s does not exist!\n" % args[1]).encode())
                pass
            continue
    
        rc = os.fork()                   # Create a child process.

        # Handling the fork. Refrence: p3-execv.py and p4-redirect.py. See COLLABORATIONS and README.
        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)
        elif rc == 0:           # This is a child.
            child(args)
        else:                   # If rc isn't 0, this is a parent.           
            if '&' in args:     # If & in args, don't wait until child dies.
                continue
            else:
                childPidCode = os.wait()        # Wait for the child to die.
                if childPidCode == 0:
                    os.write(2, ("Program terminated with exit code %d\n" % childPidCode).encode())
                    
# Child's functionalities are handled here.        
def child(args):

    pid = os.getpid()
    
    if '>' in args:      # Redirect detected. The user wants to redirect the output. Refrence: p4-redirect.
        os.close(1)                                             # Close standard output.
        sys.stdout = open(args[args.index('>') + 1], "w")       # Redirect output of program to specified text file.
        fd = sys.stdout.fileno()                                # define file descriptor
        os.set_inheritable(fd,True)                             # Set fd as inheritable
        args.remove(args[args.index('>') + 1])                  # Remove the redirect file from args
        args.remove('>')                                        # Remove the redirect char

    if '<' in args:      # Redirect detected. The user wants to redirect the input.
        os.close(0)                                             # Close standard input.
        sys.stdin = open(args[args.index('<') + 1], "r")        # Redirect input of program to specified text file.
        fd = sys.stdin.fileno()                                 # define file descriptor
        os.set_inheritable(fd,True)                             
        args.remove(args[args.index('<') + 1])                  
        args.remove('<')

    if '>>' in args:      # The user wants to append a file.
        os.close(1)
        sys.stdout = open(args[args.index('>>') + 1], "a") 
        fd = sys.stdout.fileno()                                
        os.set_inheritable(fd,True)                             
        args.remove(args[args.index('>>') + 1])                 
        args.remove('>>')

    if '&' in args:       # The user doesn't want the shell to wait until process dies. Just gets rid of '&'.               
        args.remove('&')

    if '|' in args:       # User is piping! Not quite functional.
        pr,pw = os.pipe() # Pipe: lots of help from p5-pipe. See COLLABORATIONS.md for attribution details.

        for f in (pr,pw):
            os.set_inheritable(f, True)
            os.write(2,("Pipe: pr=%d pw=%d\n" % (pr,pw)).encode())
            rc = os.fork() 

            if rc < 0:
                os.write(2,("Child fork failed.\n").encode())
            if rc == 0:
                childPipe(args,pr,pw)
            if rc > 0:
                cChildPid = os.wait()
                os.close(0)
                os.dup(pr)
                for fd in (pr,pw):
                    os.close(fd)
                    
                for line in fileinput.input():
                    os.write(2,("Pipe Child: %s" % line).encode())
                    sys.exit(1)

                    
    for char in args[0]:        # Search the command for a path.
        if '/' in args[0]:      # User specified a path - execute immmeadiately.
            program = args[0]
            try:
                os.execv(program, args)
            except FileNotFoundError:
                pass
            os.write(2, ("Child %d: Could not exec %s \n" % (pid, program)).encode())
            sys.exit(1)

    for dir in re.split(":", os.environ['PATH']):               # No path specified: try each directory. Refrence: p4-redirect.
        program = "%s/%s" % (dir, args[0])                      # Path to program is here
        try:
            os.execve(program, args, os.environ)                # Try to run the program.
        except FileNotFoundError:
            pass
    os.write(2, ("Child %d: Could not exec %s \n" % (pid, program)).encode())
    sys.exit(1)

#Child pipe method. Writes to the pipe - see README or COLLABORATIONS for attributions.
def childPipe(args,pread,pwrite): 
    os.close(1)                   # Redirect the output of this method.
    os.dup(pwrite)
    for f in (pread, pwrite):
        os.close(f)
    print("Hello! How are you?") 
    sys.exit(1)
        
parent() #Start the shell.           
