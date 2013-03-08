import sys
import requests

from pytravis import REPOS_URI, BUILDS_URI


class Repo(object):
    """Represents a repository in Travis-CI
    """
    def __init__(self, id, cache_builds=False):
        """Creates a repository object with all tha attributes returned by the API

        :cache_builds: If True, a Build object is created for each build
        """

        self._id = id
        r = requests.get(REPOS_URI + str(self._id))
        if r.headers['content-type'] == 'image/png':
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
        self.public_key = properties['public_key']
        self.slug = properties['slug']


        builds = requests.get(REPOS_URI + self.slug + "/builds").json()
        builds_dict = dict((b['id'], b) for b in builds)
        if cache_builds:
            self.builds = []
            for b in builds_dict.iterkeys():
                self.builds.append(Build(b))
        else:
            self.builds = builds_dict
            


class Build(object):
    """Represents a build in Travis-CI.
    """
    def __init__(self, id):
        self.id = id
        b = requests.get(BUILDS_URI + str(self.id))
        if b.headers['content-type'] == 'image/png':
            raise AttributeError("ERROR: Build with id %s not found!" % str(self.id))
         
        properties = b.json()
        self.status = properties['status']
        self.repository_id = properties['repository_id']
        self.committer_email = properties['committer_email']
        self.committer_name = properties['committer_name']
        self.author_email = properties['author_email']
        self.finished_at = properties['finished_at']
        self.matrix = properties['matrix']
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
