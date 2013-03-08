import requests
from prettytable import PrettyTable
import tty

from pytravis import REPOS_BY_OWNER

def get_repos_by_owner(owner):
    """Return a list of repos by owner
    """
    repos = requests.get(REPOS_BY_OWNER + str(owner)).json()
    if not repos:
        raise AttributeError("ERROR: Username %s not found!" % str(owner))
    return repos

def list_repos_by_owner(owner):
    """Print and return a list with the owner's repositories.
    """
    repos = get_repos_by_owner(owner)
    x = PrettyTable(['Name', 'ID', 'Last build ID'])
    x.align['Name'] = 'l'
    x.align['Description'] = 'l'
    for r in repos:                                        
        row = []
        [row.append(r[field]) for field in ['slug', 'id', 'last_build_id']]
        x.add_row(row)
    print x
	

def less(text, num_lines = 100):
    """Show a large text in chunks in a less-like fashion.

    param: text Text: to display
    param: num_lines: Number of lines to display in each chunk
    """
    s = str(text).split("\n")
    tty.setcbreak(sys.stdin)
    for i in range(0, len(s), self.num_lines):
        print "\n".join(s[i:i+self.num_lines])
        print "Press any key for more or <q> to exit"
        k = sys.stdin.read(1)
        if k == 'q':
            break