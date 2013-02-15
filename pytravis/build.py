import requests

class Build(object):
    """Represents a build in Travis-CI.
    """
    def __init__(self, id):
        b = requests.get("https://api.travis-ci.org/builds/%s" % str(id))
        if b.status_code != requests.status_codes.codes.OK:
            raise AttributeError("ERROR: Repository with id %s not found!" % str(id))
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
        return self._properties['matrix'][0]

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
