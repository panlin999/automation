encodings = "utf-8"
from time import sleep

import yagmail
from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread
import BeautifulReport


class TestThread(Thread):
    tests = None
    th_title = ""
    th_file = ""

    def settest(self, patte):
        self.tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern=patte)  # os.getcwd()

    def run(self) -> None:
        ###方法一
        # Run = HTMLTestRunner.HTMLTestRunner(
        #     title=self.th_title,#####"bugfree自动化测试报告",
        #     description="bugfree自动化提交bug模块",
        #     verbosity=2,
        #     stream=open(file=self.th_file, mode="w+", encoding="utf-8")
        # )
        # Run.run(self.tests)
        ###方法二
        BeautifulReport.BeautifulReport(self.tests).report(filename=self.th_file, description="测试报告")


first = TestThread()
first.settest("test_user_case.py")
first.th_file = "_bugfree测试报告1.html"
first.th_title = "第一个测试用例"

second = TestThread()
second.settest("test_user_case1.py")
second.th_file = "_bugfree测试报告2.html"
second.th_title = "第二个测试用例"

first.start()
second.start()

# yag = yagmail.SMTP(
#     host='smtp.qq.com', user='470290833@qq.com',
#     password='zafdzdhxvugfbhbh', smtp_ssl=True
# ).send('470290833@qq.com', '潘义林的测试报告', 'E:\works\demo\_bugfree自动化\_bugfree测试报告.html')
