import unittest

from test_user_case import TestCase
from bugfree_automation import bugfree_automation
from test_user_case import Testlogin
from bugfree_automation1 import bugfree_automation

suite = unittest.TestSuite
suite.addTest(unittest.makeSuite(bugfree_automation))
suite.addTest(unittest.makeSuite(bugfree_automation))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
