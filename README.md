[Travis-CI][o1] is a hosted continuous integration service for the open source community. It is integrated with GitHub and offers first class support 
for a lot of languages.

**pytravis** provides an API wrapper for python and a set of utilities to get common
information from Tracis-CI.

**Current build status**: [![Build Status](https://travis-ci.org/guillermo-carrasco/pytravis.png?branch=master)](https://travis-ci.org/guillermo-carrasco/pytravis)

_DISCLAIMER_: This project is still under development. Contributions are
very welcome :-)

##Usage
Pytravis gets the necessary information from a configuration file located in the
user's home directory. The file should be named ```.pytravisrc```. A minimal configuration
file containing the API endpoints is installed with pytravis:

```
[URI]
base_url: https://api.travis-ci.org/
repos_uri: repos/
repos_by_owner: repos.json?owner_name=
builds_uri: builds/
log_uri: jobs/{job_id}/log.txt?deansi=true
auth_github: auth/github
auth_handshake: auth/handshake
```

###Authentication
By the moment, pytravis allows authentication through a GitHub access token. To get
your GitHut token, access your GitHub account settings, go to the Applications' tab,
and copy the Personal API Access Token.

Once you have it, add an Auth section in the configuration file and paste your token
there:

```
[Auth]
github-token: your_token_here
```

**NOTE**: You can use pytravis without authentication, but you'll be able to access
only the public endpoints. Check [Travis-CI API documentation][o2] to for more details
about public and private endpoints.

[o1]: https://travis-ci.org
[o2]: https://api.travis-ci.org/docs
