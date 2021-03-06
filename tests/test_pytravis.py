import unittest
import os
from pytravis import travis, utils, gh_token

class TestPytravisObjects(unittest.TestCase):
    """Test pytravis classes
    """

    def setUp(self):
    	self.valid_repo_id = '488730'
    	self.valid_build_id = '5383366'
        self.valid_job_id = '5383367'

    @unittest.skipUnless(gh_token, "No github token")
    def test_user(self):
        """Test User class
        """
        u = travis.User()
        self.assertIsInstance(u, travis.User)

    def test_repo(self):
    	"""Test Repo class
    	"""
    	try:
    		r = travis.Repo(0)
    	except Exception as ex:
        	self.assertEqual('AttributeError', type(ex).__name__)

        r = travis.Repo(self.valid_repo_id)
        self.assertIsInstance(r, travis.Repo)
        self.assertIsInstance(r.last_build, travis.Build)
        self.assertEqual(type(r.builds), dict)
        self.assertNotEqual(len(r.builds), 0)
        r = travis.Repo(self.valid_repo_id, cache_builds=True)
        self.assertIsInstance(r.builds[0], travis.Build)


    def test_builds(self):
    	"""Test Build class
    	"""
    	try:
    		b = travis.Build(-1)
    	except Exception as ex:
    		self.assertEqual('AttributeError', type(ex).__name__)

    	b = travis.Build(self.valid_build_id)
    	self.assertIsInstance(b, travis.Build)
        for job in b.matrix:
            self.assertIsInstance(job, travis.Job)
        self.assertEqual(b.jobs, 2)


    def test_log(self):
        """Test Log class
        """
        try:
            l = travis.Log('-1', self.valid_repo_id)
        except Exception as ex:
            self.assertEqual('AttributeError', type(ex).__name__)

        l = travis.Log(self.valid_job_id, self.valid_repo_id)
        self.assertIsInstance(l, travis.Log)

        #Test different combinations of saving a log file
        logname = 'guillermo-carrasco_pytravis_' + self.valid_job_id + '.log'
        home_dir = os.environ['HOME']

        l.save()
        l.save(filename='test_filename')
        l.save(dest=home_dir)
        l.save(filename='test_filename', dest=home_dir)

        self.assertTrue(os.path.exists(logname))
        self.assertTrue(os.path.exists('test_filename'))
        self.assertTrue(os.path.exists(os.path.join(home_dir, logname)))
        self.assertTrue(os.path.exists(os.path.join(home_dir, 'test_filename')))

        #Remove created test files
        os.remove(logname)
        os.remove('test_filename')
        os.remove(os.path.join(home_dir, logname))
        os.remove(os.path.join(home_dir, 'test_filename'))


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