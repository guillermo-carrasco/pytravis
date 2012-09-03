import json
import urllib

########################
# Travis API addresses #
########################
urlBase = 'http://travis-ci.org/'

repos = urlBase + 'repositories.json'
reposByOwner = urlBase + 'repositories.json?owner_name={owner}'
reposIndexSearch = urlBase + 'repositories.json?search={query}'
reposShow = urlBase + '{owner_name}/{name}.json'
builds = urlBase + '{owner_name}/{name}/builds.json'
buildsShow = urlBase + '{owner_name}/{name}/builds/{id}.json'
workers = urlBase + 'workers.json'
jobs = urlBase + 'jobs.json'
jobsShow = urlBase + 'jobs/{id}.json'


def getBuildsAndJobs(_owner):
    """
    Returns a list with all the owner's builds
    """
    repos = json.loads(urllib.urlopen(reposByOwner.format(owner=_owner)).read())
    buildsList = []
    runningList = []
    jobsList = []

    # Build the builds list
    for repo in repos:
        buildsPerRepo = json.loads(urllib.urlopen(builds.format(owner_name=_owner, name=repo['slug'].split('/')[-1])).read())
        for build in buildsPerRepo:
            build['repository'] = repo['slug'].split('/')[-1]
            if build['state'] == 'started':
                runningList.append(build)
            buildsList.append(build)

    # Build running jobs list
    for r in runningList:
        jobID = json.loads(urllib.urlopen(buildsShow.format(owner_name=_owner, name=r['repository'], id=r['id'])).read())['matrix'][0]['id']
        job = json.loads(urllib.urlopen(jobsShow.format(id = jobID)).read())
        job['repository'] = r['repository']
        jobsList.append(job)

    return buildsList, jobsList