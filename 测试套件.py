import unittest
from _bugfree自动化.test_user_case import Testlogin
from _bugfree自动化.test_user_case1 import Testlogin1

###创建测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Testlogin))
suite.addTest(unittest.makeSuite(Testlogin1))

if __name__ == '__main__':
    ###运行时输出详细信息。verbosity=2  默认为1 0表示不输出错误信息 2表述输出错误详细信息
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
