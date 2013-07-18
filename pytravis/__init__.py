import ConfigParser
import requests
import json
import os

#Load all mutable-like information from configuration files
conf_file = os.path.join(os.environ["HOME"], ".pytravisrc")
gh_token = False
auth_token = False
if os.path.exists(conf_file):
    conf = ConfigParser.ConfigParser()
    conf.read(conf_file)
    #Get API endpoints
    try:
        urls = dict(conf.items('URI'))
        base_url = urls.get("base_url")
        repos_uri = base_url + urls.get("repos_uri")
        builds_uri = base_url + urls.get("builds_uri")
        log_uri = base_url + urls.get("log_uri")
        repos_by_owner = base_url + urls.get("repos_by_owner")
        auth_github = base_url + urls.get("auth_github")
        auth_handshake = base_url + urls.get("auth_handshake")
        users_uri = base_url + urls.get("users_uri")

    except ConfigParser.NoSectionError:
        raise RuntimeError("The configuration file doesn't seem to contain the \
            Travis-CI URI endpoints.")
    try:
        gh_token = conf.get('Auth', 'github-token')
    except ConfigParser.NoSectionError:
        gh_token = False
    if gh_token:
        #Getting Travis-CI Authorization token
        post_tk = requests.post(auth_github, data={'github_token': gh_token})
        if post_tk.status_code == requests.codes.NOT_FOUND:
            raise AttributeError("Seems to be an error with the GitHub token, please \
                check that the GitHub token is correctly placed in the configuration file")
        auth_token = json.loads(post_tk.content)
        #Ensure that Travis-CI has given access to pytravis
        handshake = requests.get(auth_handshake)
        if handshake.status_code == requests.codes.NOT_FOUND:
            raise AttributeError("There was something wrong with Travis-CI Authentication, \
                please check that your GitHub token is correctly placed in the configuration file")

else:
    raise RuntimeError("Not configuration file found, please ensure that you have \
        a ~/.pytravisrc configuration file.")