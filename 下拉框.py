import select
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("http://www.jasonisoft.cn/bugfree/index.php/site/login")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys("PanYiLin")
driver.find_element_by_id("LoginForm_password").send_keys("123456")
driver.find_element_by_id("LoginForm_rememberMe").click()
driver.find_element_by_id("SubmitLoginBTN").click()
time.sleep(2)
##进入界面  下拉框选择
el1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/select")
# 使用name属性找到页面上name属性为“fruit”的下拉列表元素
# Select(el1).select_by_index(1)
###使用select_by_visible_text必须文本相等，如何后面有空格也必须相等
Select(el1).select_by_visible_text('建筑材料库房管理系统-2组（汪蒙）')
# Select(el1).select_by_value("667")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/a").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/div[1]/div[1]/input").send_keys("121312311")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/div[1]/div[2]/select[1]/optgroup/option[5]").click()
driver.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/div[1]/div[2]/select[2]/option[3]").click()
# el2=driver.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/div[1]/div[2]/select[1]")
# Select(el2).select_by_value("8016")
# el3=driver.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/div[1]/div[2]/select[2]")
# Select(el3).select_by_value("8018")

print(driver.current_url)

time.sleep(5)
driver.quit()
