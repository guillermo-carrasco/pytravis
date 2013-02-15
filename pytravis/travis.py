import requests

base_url = "https://api.travis-ci.org/"
repos_url = base_url + "/repos/"

class Repo(object):
    """Represents a repository in Travis-CI
    """
    def __init__(self, id):
        r = requests.get(repos_url + str(id))
        if r.status_code != requests.status_codes.codes.OK:
            raise AttributeError("ERROR: Repository with id %s not found!" % str(id))
        self._properties = r.json()

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
    