import sys
import requests

from pytravis import REPOS_URI, BUILDS_URI


class Repo(object):
    """Represents a repository in Travis-CI
    """
    def __init__(self, id):
        self._id = id
        self.update()

    def update(self):
        """Update information of the repository.

        Update information of the repository: Builds, last builds, etc.
        """
        r = requests.get(REPOS_URI + str(self._id))
        if not r.status_code == requests.status_codes.codes.OK:
            raise AttributeError("ERROR: Repository with id %s not found!" % str(self._id))
        self._properties = r.json()
        builds = requests.get(REPOS_URI + self._properties['slug'] + "/builds").json()
        self.builds_list = dict((b['id'], b) for b in builds)

    @property
    def description(self):
        return self._properties['description']

    @property
    def id(self):
        return self._properties['id']

    @property
    def last_build_duration(self):
        return self._properties['last_build_duration']

    @property
    def last_build_finished_at(self):
        return self._properties['last_build_finished_at']

    @property
    def last_build_id(self):
        return self._properties['last_build_id']

    @property
    def last_build_language(self):
        return self._properties['last_build_language']

    @property
    def last_build_number(self):
        return self._properties['last_build_number']

    @property
    def last_build_result(self):
        return self._properties['last_build_result']

    @property
    def last_build_started_at(self):
        return self._properties['last_build_started_at']

    @property
    def last_build_status(self):
        return self._properties['last_build_status']

    @property
    def public_key(self):
        return self._properties['public_key']

    @property
    def slug(self):
        return self._properties['slug']

    def get_builds(self):
        """Obtain the list of builds for that repository.
        """
        return self.builds_list


class Build(object):
    """Represents a build in Travis-CI.
    """
    def __init__(self, id):
        b = requests.get(BUILDS_URI + str(id))
        if b.status_code != requests.status_codes.codes.OK:
            raise AttributeError("ERROR: Build with id %s not found!" % str(id))
        self._properties = b.json()

    @property
    def status(self):
        return self._properties['status']

    @property
    def repository_id(self):
        return self._properties['repository_id']

    @property
    def committer_email(self):
        return self._properties['committer_email']

    @property
    def committer_name(self):
        return self._properties['committer_name']

    @property
    def author_email(self):
        return self._properties['author_email']

    @property
    def finished_at(self):
        return self._properties['finished_at']

    @property
    def matrix(self):
        return self._properties['matrix']

    @property
    def number(self):
        return self._properties['number']

    @property
    def author_name(self):
        return self._properties['author_name']

    @property
    def compare_url(self):
        return self._properties['compare_url']

    @property
    def committed_at(self):
        return self._properties['committed_at']

    @property
    def state(self):
        return self._properties['state']

    @property
    def result(self):
        return self._properties['result']

    @property
    def branch(self):
        return self._properties['branch']

    @property
    def duration(self):
        return self._properties['duration']

    @property
    def commit(self):
        return self._properties['commit']

    @property
    def message(self):
        return self._properties['message']

    @property
    def started_at(self):
        return self._properties['started_at']

    @property
    def config(self):
        return self._properties['config']

    @property
    def id(self):
        return self._properties['id']

    @property
    def event_type(self):
        return self._properties['event_type']