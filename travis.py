import json
import urllib
import re


class TravisManager:
    """Get information from Travis-CI
    """
    def __init__(self):
        self.urlBase = 'http://travis-ci.org/'
        self.repos = self.urlBase + 'repositories.json'
        self.reposByOwner = self.urlBase + 'repositories.json?owner_name={owner}'
        self.reposIndexSearch = self.urlBase + 'repositories.json?search={query}'
        self.reposShow = self.urlBase + '{owner_name}/{name}.json'
        self.builds = self.urlBase + '{owner_name}/{name}/builds.json'
        self.buildsShow = self.urlBase + '{owner_name}/{name}/builds/{id}.json'
        self.workers = self.urlBase + 'workers.json'
        self.jobs = self.urlBase + 'jobs.json'
        self.jobsShow = self.urlBase + 'jobs/{id}.json'

    def getRepos(self, _owner):
        """Return a list with the owner's repositories
        """
        return json.loads(urllib.urlopen(self.reposByOwner.format(owner = _owner)).read())


    def getBuildList(self, _owner, _repo):
        """Returns a list with all the builds for the _owner's  _repo
        """
        return json.loads(urllib.urlopen(self.builds.format(owner_name=_owner, name=_repo)).read())


    def getBuildsAndJobs(self, _owner):
        """
        Returns a list with all the owner's builds
        """
        repos = json.loads(urllib.urlopen(self.reposByOwner.format(owner=_owner)).read())
        buildsList = []
        runningList = []
        jobsList = []

        # Build the builds list
        for repo in repos:
            buildsPerRepo = json.loads(urllib.urlopen(self.builds.format(owner_name=_owner, name=repo['slug'].split('/')[-1])).read())
            for build in buildsPerRepo:
                build['repository'] = repo['slug'].split('/')[-1]
                if build['state'] == 'started':
                    runningList.append(build)
                buildsList.append(build)

        # Build running jobs list
        for r in runningList:
            jobID = json.loads(urllib.urlopen(self.buildsShow.format(owner_name=_owner, name=r['repository'], id=r['id'])).read())['matrix'][0]['id']
            job = json.loads(urllib.urlopen(self.jobsShow.format(id = jobID)).read())
            job['repository'] = r['repository']
            jobsList.append(job)

        return buildsList, jobsList

    def getRelatedJob(self, owner, repo, buildID):
        """
        Return the job releted to the build <buildID> of the owner's <owner> repo <repo>
        """
        jobID = json.loads(urllib.urlopen(self.buildsShow.format(owner_name=owner, name=repo, id=buildID)).read())['matrix'][0]['id']
        return json.loads(urllib.urlopen(self.jobsShow.format(id=jobID)).read())

    def getFormattedLog(self, log):
        """Return a log ready to be written to a file: Without control characters
        """
        return re.sub(r"(?m)^.*\r(?!$)", "", log).encode('utf8').replace('\r', '')