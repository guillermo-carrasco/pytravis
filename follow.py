# follow.py
#
# Follow a file like tail -f.

import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

# Example use
# Note : This example requires the use of an apache log simulator.
# 
# Go to the directory run/foo and run the program 'logsim.py' from
# that directory.   Run this program as a background process and
# leave it running in a separate window.  We'll write program
# that read the output file being generated
# 

if __name__ == '__main__':
    logfile = open("test.log","r")
    loglines = follow(logfile)
    for line in loglines:
        print line,

    
