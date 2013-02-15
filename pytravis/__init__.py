import platform
import tty
import sys

class Less(object):
    """Class to show a large text in chunks in a less-like fashion.
    """
    def __init__(self, num_lines=100):
        self.num_lines = num_lines

    def less(self, other):
        """Show the text chunk by chunk.

        param: other Text to display
        """
        s = str(other).split("\n")
        tty.setcbreak(sys.stdin)
        for i in range(0, len(s), self.num_lines):
            print "\n".join(s[i:i+self.num_lines])
            print "Press any key for more or <q> to exit"
            k = sys.stdin.read(1)
            if k == 'q':
                break