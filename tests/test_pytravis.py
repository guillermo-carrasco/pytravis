import unittest
from pytravis import travis, utils


class TestPytravisObjects(unittest.TestCase):
    """Test pytravis classes
    """

    def setUp(self):
    	self.pytravis_id = '488730'
    	self.pytravis_build_id = '5278830'

    def tests_repo(self):
    	"""Test Repo class
    	"""
    	try:
    		r = travis.Repo(0)
    	except Exception as ex:
        	self.assertEqual('AttributeError', type(ex).__name__)

        r = travis.Repo(self.pytravis_id)
        self.assertIsInstance(r, travis.Repo)
        self.assertEqual(type(r.builds), dict)
        self.assertNotEqual(len(r.builds), 0)
        r = travis.Repo(self.pytravis_id, cache_builds=True)
        self.assertIsInstance(r.builds[0], travis.Build)

    def test_builds(self):
    	"""Test Build class
    	"""
    	try:
    		b = travis.Build(-1)
    	except Exception as ex:
    		self.assertEqual('AttributeError', type(ex).__name__)

    	b = travis.Build(self.pytravis_build_id)
    	self.assertIsInstance(b, travis.Build)

    	#Test a build with a matrix!

class TestUtils(unittest.TestCase):
	"""Test pytrtavis utils
	"""
	def setUp(self):
		self.owner = 'guillermo-carrasco'

	def test_get_repos_by_owner(self):
		"""Test get_repos_by_owner functionality
		"""
		try:
			r = utils.get_repos_by_owner('I_do_not_exist_as_owner_of_a_repo')
		except Exception as ex:
			self.assertEqual('AttributeError', type(ex).__name__)

		r = utils.get_repos_by_owner(self.owner)
		self.assertEqual(type(r), list)