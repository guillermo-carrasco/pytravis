#Overview
[Travis-CI][o1] is a hosted continuous integration service for the open source community. It is integrated with GitHub and offers first class support 
for a lot of languages.

TravisTracker provides you a command line interface to check your repositories' builds in an interactive way, without the
necessity of a web berowser, or even desktop environment (good news sysadmins!).

#Use
You can get the list of command line options typing:

        python tracker.py -h

##Get a build's log
To get a build's log, use the __getlog__ functionality.

        python tracker.py [-o OWNER] [-r REPOSITORY] getlog

If you don't specify owner and/or repository, TravisTracker will ask you for them:

        > python tracker.py getlog
        > Please insert the repository owner's name:
        > Listing repositories...
        > bcbio-nextgen-deploy
        > bcbb
        > bcbb_chapmanb
        > From which repository do you want to save a log?: 

Don't worry about typos, TravisTracker can handle them:

        > python tracker.py -o guillermo_carrasco getlog
        > This username doesn't appear to exist, please insert a correct username:

When owner and repository has been correctly introduced, just remains to select one of your builds to save its log to a file:

        > python tracker.py -o guillermo-carrasco -r bcbb getlog
        > (TravisTrackes show a list with your builds)
        > Please, enter the number of the build you want to save the log: 18
        > Saving build 18 into logs/guillermo-carrasco_bcbb_18_.log


[o1]: https://travis-ci.org
