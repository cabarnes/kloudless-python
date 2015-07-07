import kloudless
import unittest
import os
import utils

API_KEY = os.environ['API_KEY']
kloudless.configure(api_key=API_KEY)

accounts = utils.get_account_for_each_service()

class Search(unittest.TestCase):
    pass

if __name__ == '__main__':
    suite = utils.create_suite([utils.create_test_case(acc, Search) for acc in accounts])
    unittest.TextTestRunner(verbosity=2).run(suite)
