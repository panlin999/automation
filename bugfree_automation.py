# from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class bugfree_automation:
    # driver=webdriver.Chrome()
    # driver.get("http://www.jasonisoft.cn/bugfree/index.php/site/login")
    # driver.maximize_window()
    # sleep(1)
    # try:
    def __init__(self, driver):
        self.driver = driver

    # 2个账号登录成功，1个登录失败
    def login0(self, name, passwd):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(name)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/input").send_keys(
            passwd)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr[6]/td[2]/input").click()

    # 获取结果
    # 成功的断言
    def getSuccessDate(self):
        return self.driver.title

    # 失败的断言
    @property
    def getErrorData(self):
        return self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr[1]/td/div").text

    # # 创建一个bug
    def create_bug(self, name, passwd, c0, c1, c2, c3, c4, c5, c6, c7):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(name)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/input").send_keys(
            passwd)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table/tbody/tr[6]/td[2]/input").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/select/option[2]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/a").click()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/div[1]/div[1]/input").send_keys(
            c0)  # .perform() #.perform()执行的意思
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/form/div[1]/div[1]/div[2]/select[1]/optgroup/option[2]").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/div[1]/div[2]/select[1]").click()
        sleep(1)
        # clear()清空输入框
        self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/fieldset/div[2]/input").clear()
        self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/fieldset/div[2]/input").send_keys(c1)
        sleep(1)
        self.driver.find_element_by_id("BugInfoView_severity").send_keys(c2)
        # js = "var q=document.body.scrollTop=10000"
        # self.driver.execute_script(js)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/fieldset/div[5]/select").send_keys(c3)
        sleep(1)
        ######滚动条
        # 滚动条拉到最底,防止找不到元素
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        # 跳入第一个内联框架
        # self.driver.switch_to.frame(测试)
        self.driver.switch_to.frame(
            self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/fieldset[1]/div/div/div[2]/iframe"))
        self.driver.find_element_by_xpath("/html/body").send_keys(c4)
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(
            self.driver.find_element_by_xpath('//*[@id="bug-info-form"]/div[3]/fieldset[2]/div/div/div[2]/iframe'))
        # driver.find_element_by_xpath("/html/body/ol[1]/li").click()

        # 拖动滚动条
        # ac.click_and_hold(self.driver.find_element_by_xpath("")).move_by_offset()
        # js = "var q=document.getElementById('id').scrollTop=10000"
        # self.driver.execute_script(js)
        # js = "var q=document.documentElement.scrollTop=10000"
        # self.driver.execute_script(js)
        # target = self.driver.find_element_by_id("id_keypair")  # 需要将滚动条拖动至的指定的元素对象定位
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 将滚动条拖动到元素可见的地方
        # from selenium.webdriver.common.keys import Keys  # 导入Keys类
        # self.driver.find_element_by_id("id_login_method_0").send_keys(Keys.TAB)  # 定位元素并操作输入
        # # 执行这段代码，会获取到当前窗口总高度
        # js = "return action=document.body.scrollHeight"
        # # 初始化现在滚动条所在高度为0
        # height = 0
        # # 当前窗口总高度
        # new_height = self.driver.execute_script(js)
        #
        # while height < new_height:
        #     # 将滚动条调整至页面底部
        #     for i in range(height, new_height, 1000):
        #         self.driver.execute_script('window.scrollTo(0, {})'.format(i))
        #         sleep(0.5)
        #     height = new_height
        #     sleep(2)
        #     new_height = self.driver.execute_script(js)
        ac = ActionChains(self.driver)
        one = self.driver.find_element_by_xpath("/html/body/ol[1]/li")
        ac.click(one).send_keys(c5).perform()
        sleep(2)
        twe = self.driver.find_element_by_xpath("/html/body/ol[2]/li")
        ac.click(twe).send_keys(c6).perform()
        sleep(2)
        three = self.driver.find_element_by_xpath("/html/body/ol[3]/li")
        ac.click(three).send_keys(c7).perform()
        sleep(2)
        # four=driver.find_element_by_xpath("/html/body/text()[4]")
        # ac.click(four).send_keys("333333").perform()
        # 跳出内联框架
        # self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()
        # 滚动条拉到最顶部,防止找不到元素
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/input[1]").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/form/div[2]/div[2]/fieldset[2]/div[1]/input").send_keys("123456")
        self.driver.back()

        # except:
        #     print("出错！")

        sleep(3)
        self.driver.quit()

    def getcreateSuccessData(self):
        return self.driver.find_element_by_id("span_info_id").text
