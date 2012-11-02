#!/usr/bin/env python

import traivs

t = travis.TravisManager()

def _getLog(owner, repo=None, jobID=None):
    """Save a log to a file. 
        If repo and jobID are specified, then the log is directly saved to disk (if no errors). Otherwise, the program ask the user until
        all the necessary information has been obtained.
    """

def _followLog():
    """Keeps printing a non-finished build's log.
    """

if __name__ == '__main__':
    #Parse arguments, and execute corresponding functions
