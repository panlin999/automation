import time
import unittest
# ####处理滚动条的网址：https://www.freesion.com/article/67411232832/，第一个最有用
# 滚动进入条至最右边
#### def scroll_right(self):
# ##    js = "window.scrollTo(1000,10000)"  # 参数是左边距，和上边距
#  #####   return self.driver.execute_script(js)
####import self as self
import xlrd
from selenium import webdriver
from xlutils.copy import copy
from ddt import ddt
from ddt import data
from ddt import unpack
from bugfree_automation import bugfree_automation
from method import method
from login import login
from unittest import TestCase
import threading


# from method import method
@ddt
class Testlogin(TestCase):
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.jasonisoft.cn/bugfree/index.php/site/login")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ##登录界面
    @data(*login.SuccessData1)
    @unpack
    def testSucceceLogin(self, ID, a, b, c):
        print("登录成功的正例")
        username = a
        print(username)
        passwd = b
        expect = c
        # 打开浏览器

        # driver.set_window_size(800, 500)
        # driver.switch_to.parent_frame()
        # 执行测试
        login = bugfree_automation(self.driver)
        login.login0(username, passwd)
        # 结果
        result = login.getSuccessDate()

        if expect == result:
            c0 = xlrd.open_workbook(filename="bugfree_login.xls")
            c1 = copy(c0)
            c2 = c1.get_sheet(0)
            c2.write(ID, 4, "通过")
            c1.save("bugfree_login.xls")
        else:
            c0 = xlrd.open_workbook(filename="bugfree_login.xls")
            c1 = copy(c0)
            c2 = c1.get_sheet(0)
            c2.write(ID, 4, "不通过")
            c1.save("bugfree_login.xls")
        self.assertEqual(expect, result)

    @data(*login.ErrorData1)
    @unpack
    def testErrorLogin(self, ID, a, b, c):
        username = a
        passwd = b
        expect = c
        # 获取浏览器驱动
        # driver = webdriver.Chrome()
        # driver.get("http://www.jasonisoft.cn/bugfree/index.php/site/login")
        # driver.maximize_window()
        # driver.set_window_size(800, 500)
        # 进行登录测试
        login = bugfree_automation(self.driver)
        login.login0(username, passwd)
        # 返回结果
        result = login.getErrorData
        if expect == result:
            c0 = xlrd.open_workbook("bugfree_login.xls")
            c1 = copy(c0)
            c2 = c1.get_sheet(1)
            c2.write(ID, 4, "通过")
            c1.save("bugfree_login.xls")
        else:
            c0 = xlrd.open_workbook("bugfree_login.xls")
            c1 = copy(c0)
            c2 = c1.get_sheet(1)
            c2.write(ID, 4, "不通过")
            c1.save("bugfree_login.xls")
        self.assertEqual(expect, result)

    # ###  # 创建一个新的bug
    ##### @data(*login.SuccessData2)
    ######@unpack
    @data(*method.SuccessData)
    @unpack
    def testcreate_bug(self, ID, a, b, c, c0, c1, c2, c3, c4, c5, c6, c7):
        username = a
        passwd = b
        expect = c
        # 创建浏览器
        # driver = webdriver.Chrome()
        # driver.get("http://www.jasonisoft.cn/bugfree/index.php/site/login")
        #
        # driver.maximize_window()
        # driver.set_window_size(800, 500)
        time.sleep(3)
        # self.driver.set_window_size(1080,900)
        self.driver.implicitly_wait(8)
        time.sleep(3)
        self.driver.refresh()
        print("刷新页面")
        # 执行测试
        create_bug = bugfree_automation(self.driver)
        create_bug.create_bug(username, passwd, c0, c1, c2, c3, c4, c5, c6, c7)

        c0 = xlrd.open_workbook("建筑材料管理系统.xls")
        c1 = copy(c0)
        c2 = c1.get_sheet(0)
        c2.write(ID, 12, "通过")
        c1.save("建筑材料管理系统.xls")

    #     # 断言
    #     # result = create_bug.getcreateSuccessData()
    # #     # if expect == result:
    # #     #     c0 = xlrd.open_workbook("建筑材料管理系统.xls")
    # #     #     c1 = copy(c0)
    # #     #     c2 = c1.get_sheet(0测试)
    # #     #     c2.write(ID, 12, "通过")
    # #     #     c1.save("建筑材料管理系统.xls")
    # #     # else:
    # #     #     c0 = xlrd.open_workbook("建筑材料管理系统.xls")
    # #     #     c1 = copy(c0)
    # #     #     c2 = c1.get_sheet(0测试)
    # #     #     c2.write(ID, 12, "不通过")
    # #     #     c1.save("建筑材料管理系统.xls")
    # #     # self.assertEqual(expect,result)
    def tearDown(cls) -> None:
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
    # # 多线程
    # t1 = threading.Thread(target=self.testSucceceLogin, name="thread1")
    # t2 = threading.Thread(target=self.testErrorLogin, name="thread1")
    # t3 = threading.Thread(target=self.testcreate_bug, name="thread1")
    # start_time = time.time()
    # t1.start()
    # t1.join()
    # t2.start()
    # print("当前活跃的线程有：{}".format(threading.currentThread()))
    # print("正在运行的所有线程有：{}".format(threading.enumerate()))
    # print("正在运行的线程数量有：{}".format(threading.active_count()))
    # t2.join()
    # end_time = time.time()
    # print("程序运行耗时：{}".format(end_time - start_time))
