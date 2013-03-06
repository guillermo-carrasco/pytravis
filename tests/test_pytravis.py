import unittest
from pytravis import travis


class TestPytravisObjects(unittest.TestCase):
    """Test functionalities of pytravis classes
    """

    def tests_repo(self):
    	try:
    		r = travis.Repo(0)
    	except Exception as ex:
        	self.assertEqual('AttributeError', type(ex).__name__)
