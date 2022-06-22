import time

encodings = "utf-8"
from time import sleep
import yagmail
from HTMLTestRunner import HTMLTestRunner
import unittest
import os

if __name__ == '__main__':
    tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test*.py")  # os.getcwd()
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    file = open(file=os.getcwd() + '/' + nowtime + "_bugfree测试报告.html", mode="w+", encoding="utf-8")
    Run = HTMLTestRunner.HTMLTestRunner(
        title="bugfree自动化测试报告",
        description="bugfree自动化提交bug模块",
        verbosity=1,
        stream=file
    )
    Run.run(tests)

# Run = HTMLTestRunner.HTMLTestRunner(
#     title="bugfree自动化测试报告",
#     description="bugfree自动化提交bug模块",
#     verbosity=1,
#     stream=open(file="_bugfree测试报告.html", mode="w+", encoding="utf-8")
# )
# Run.run(tests)

# yag = yagmail.SMTP(
#     host='smtp.qq.com', user='470290833@qq.com',
#     password='zafdzdhxvugfbhbh', smtp_ssl=True
# ).send('470290833@qq.com', '潘义林的测试报告', 'E:\works\demo\_bugfree自动化\_bugfree测试报告.html')
