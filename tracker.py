#!/usr/bin/env python

import json

import travis
import argparse


def _getLog(owner=None, repo=None, jobID=None):
    """Save a log to a file. 
    If owner, repo and jobID are specified, then the log is directly saved to disk (if no errors). Otherwise, 
    the program ask the user until all the necessary information has been obtained.
    """
    if not owner:
        owner = raw_input("Please insert the repository owner's name: ")
    if not repo:
        print 'Listing repositories...'
        t = travis.TravisManager()
        repos = t.getRepos(owner)
        # Build the list of repositories
        l = []
        [l.append(r['slug'].split('/')[1]) for r in repos]
        print '\n'.join(l)
        while not repo in l:
            repo = raw_input('From which repository do you want to save a log?: ')
    if not jobID:
        print 'Listing repository builds...'
    


def _followLog():
    """Keeps printing a non-finished build's log.
    """


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Diferent utilities to track Travis-CI logs and builds')
    #Positional arguments (mutual exclusive)
    sp = parser.add_subparsers(dest = 'command')
    sp.add_parser('getlog', help="Save a logo to disk.")
    sp.add_parser('follow', help = "Keeps printing a non-finished build's log")
    #Optional arguments
    parser.add_argument('-o', '--owner', help="Owner of the repository to track")
    parser.add_argument('-r', '--repository', help = "Repository to track")
    parser.add_argument('-i', '--id', help = "ID of the build or job to track")
    
    args = parser.parse_args()
    if args.command == 'getlog':
        _getLog(owner = args.owner, repo = args.repository, jobID = args.id)
