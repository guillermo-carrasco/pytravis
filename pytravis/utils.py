import requests
import tty

from pytravis import REPOS_BY_OWNER

def list_repos_by_owner(owner):
	"""Return a list with the owner's repositories.
	"""
	repos = requests.get(REPOS_BY_OWNER + str(owner)).json()
	if not repos:
		raise AttributeError("ERROR: Username %s not found!" % str(owner))
	return 
	

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