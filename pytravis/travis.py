import sys
import os
import requests

from pytravis import repos_uri, builds_uri, log_uri, users_uri, gh_token, auth_token

class User(object):
    """Represents a user in Travis-CI
    """
    def __init__(self):
        if not gh_token:
            raise RuntimeError("Cannot create a User object without authenticating")
        r = requests.get(users_uri, params=auth_token)
        if r.status_code == requests.codes.NOT_FOUND:
            raise AttributeError("Could not create User object")

        properties = r.json()
        self.email = properties['email']
        self.gravatar_id = properties['gravatar_id']
        self.is_syncing = properties['is_syncing']
        self.locale = properties['locale']
        self.login = properties['login']
        self.name = properties['name']
        self.synced_at = properties['synced_at']

    #TODO: Add functions to get user info: repos, builds, etc...

class Repo(object):
    """Represents a repository in Travis-CI
    """
    def __init__(self, id, cache_builds=False):
        """Creates a repository object with all tha attributes returned by the API

        :cache_builds: If True, a Build object is created for each build
        """
        self._id = id
        r = requests.get(repos_uri + str(self._id))
        if r.status_code == requests.codes.NOT_FOUND:
            raise AttributeError("Repository with id %s not found!" % str(self._id))

        properties = r.json()
        self.description = properties['description']
        self.id = properties['id']
        self.last_build_duration = properties['last_build_duration']
        self.last_build_finished_at = properties['last_build_finished_at']
        self.last_build_id = properties['last_build_id']
        self.last_build_language = properties['last_build_language']
        self.last_build_number = properties['last_build_number']
        self.last_build_result = properties['last_build_result']
        self.last_build_started_at = properties['last_build_started_at']
        self.last_build_status = properties['last_build_status']
        self.last_build = Build(self.last_build_id)
        self.public_key = properties['public_key']
        self.slug = properties['slug']

        builds = requests.get(repos_uri + self.slug + "/builds").json()
        self.builds_dict = dict((b['id'], b) for b in builds)
        if cache_builds:
            self.builds = []
            for b in self.builds_dict.iterkeys():
                self.builds.append(Build(b))
            self.builds_cached = True
        else:
            self.builds = self.builds_dict
            self.builds_cached = False

    def cache_builds(self):
        """Cache all the builds.
        """
        if not self.builds_cached:
            self.builds = []
            for b in builds_dict.iterkeys():
                self.builds.append(Build(b))


class Build(object):
    """Represents a build in Travis-CI.
    """
    def __init__(self, id):
        self.id = id
        b = requests.get(builds_uri + str(self.id))
        if b.status_code == requests.codes.NOT_FOUND:
            raise AttributeError("ERROR: Build with id %s not found!" % str(self.id))
         
        properties = b.json()
        self.status = properties['status']
        self.repository_id = properties['repository_id']
        self.committer_email = properties['committer_email']
        self.committer_name = properties['committer_name']
        self.author_email = properties['author_email']
        self.finished_at = properties['finished_at']
        self.matrix = []
        for job in properties['matrix']:
            self.matrix.append(Job(job))
        self.jobs = len(self.matrix)
        self.number = properties['number']
        self.author_name = properties['author_name']
        self.compare_url = properties['compare_url']
        self.committed_at = properties['committed_at']
        self.state = properties['state']
        self.result = properties['result']
        self.branch = properties['branch']
        self.duration = properties['duration']
        self.commit = properties['commit']
        self.message = properties['message']
        self.started_at = properties['started_at']
        self.config = properties['config']
        self.id = properties['id']
        self.event_type = properties['event_type']


class Job(object):
    """Represents a Job in Travis-CI
    """
    def __init__(self, properties):
        self.allow_failure = properties['allow_failure']
        self.config = properties['config']
        self.finished_at = properties['finished_at']
        self.id = properties['id']
        self.number = properties['number']
        self.repository_id = properties['repository_id']
        self.result = properties['result']
        self.started_at = properties['started_at']
        self.log = Log(self.id, self.repository_id)


class Log(object):
    """Represents a log and some functionalities
    """
    def __init__(self, id, repository_id):
        req = requests.get(log_uri.format(job_id=id))
        if req.status_code == requests.status_codes.codes.NOT_FOUND:
            raise AttributeError("A Job with this id does not exist")
        self.id = id
        self.content = req.content
        self.repository_id = repository_id

    def save(self, filename='', dest=''):
        """Saves the log to disk.

        :filename: Name of the file to save. By default <repo_name>_<job_id>.log
        :dest: Where to save the log
        """
        if not filename:
            filename = Repo(self.repository_id).slug.replace('/', '_') + \
                    '_' + str(self.id) + '.log'
        if dest and not os.path.exists(dest):
            raise IOError("The specified destiny directory doesn't exists")

        with open(os.path.join(dest, filename), 'w') as log:
            for l in self.content:
                log.writelines(l)

    def update(self):
        """Updates the content the Log
        """
        self.content = requests.get(log_uri.format(job_id=id)).content