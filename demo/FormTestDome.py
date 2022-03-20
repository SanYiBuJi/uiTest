# -*- coding:utf-8 -*-
# Author : SanYiBuJi
# Data : 2022/3/13 22:51
from selenium import webdriver
from time import sleep

from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select

from config import Config


class FormTestDome:
    '''
    测试http://sahitest.com/demo/formTest.htm 中的元素定位练习
    Test the elements in the http://sahitest.com/demo/formTest.htm location practice
    '''

    TestURl = "http://sahitest.com/demo/formTest.htm"
    def __init__(self):
        # self.drvice = webdriver.Chrome(Config.driver_path)
        self.drvice = webdriver.Chrome("D:\\Tools\\WebDriver\\chromedriver.exe")
        self.drvice.get(FormTestDome.TestURl)
        # 处理弹窗
        self.drvice.switch_to.alert.accept()

    def quit(self):
        self.drvice.quit()

    def input_name(self):
        element = self.drvice.find_element_by_name("t1")
        element.clear()
        element.send_keys("测试输入")
        sleep(3)

    def input_xpath(self):
        element = self.drvice.find_element_by_xpath("//html/body/form/table/tbody/tr[3]/td[2]/input")
        element.clear()
        element.send_keys("测试输入")
        sleep(3)

    def input_css_name(self):
        element = self.drvice.find_element_by_css_selector("input[name='name']")
        element.clear()
        element.send_keys("测试输入")
        sleep(3)

    def input_css_name2(self):
        element = self.drvice.find_element_by_css_selector("input[name='$a_dollar']")
        element.clear()
        element.send_keys("测试输入")
        sleep(3)

    def input_css_attribute(self):
        element = self.drvice.find_element_by_css_selector("input[disabled='true']")
        print(element.get_attribute("name"))

    def input_css_attribute2(self):
        element = self.drvice.find_element_by_css_selector("input[readonly]")
        print(element.get_attribute("name"))

    def input_css_type(self):
        element = self.drvice.find_element_by_css_selector("input[type='textarea']")
        element.clear()
        element.send_keys("测试输入")
        sleep(3)

    # 这个input标签的type值不对,跳过
    def input_css_type2(self):
        element = self.drvice.find_element_by_css_selector("input[type='invalid']")
        element.clear()
        element.send_keys("测试输入")
        sleep(3)

    def textarea_input(self):
        element = self.drvice.find_element_by_name("ta1")
        element.clear()
        element.send_keys("策就是看接口连接上的可乐放家里卡萨丁解放路口设计的反馈了时间到付款时间到了会计法律上的解放撒旦教弗兰克萨吉林科技反倒是拉科技大飞机上的发送地方就是劳动纠纷涉及的法律斯卡迪复健科拉萨的减肥")
        sleep(3)
        element2 = self.drvice.find_element_by_xpath("//textarea[2]")
        element2.clear()
        element2.send_keys("策就是看接口连接上的可乐放家里卡萨丁解放路口设计的反馈了时间到付款时间到了会计法律上的解放撒旦教弗兰克萨吉林科技反倒是拉科技大飞机上的发送地方就是劳动纠纷涉及的法律斯卡迪复健科拉萨的减肥")
        sleep(3)

    def checkbox_dome(self):
        element1 = self.drvice.find_element_by_css_selector("input[value='cv1']")
        element1.click()
        sleep(3)
        element2 = self.drvice.find_element_by_css_selector("input[value='cv2']")
        element2.click()
        sleep(3)
        element3 = self.drvice.find_element_by_css_selector("input[value='cv3']")
        element3.click()
        sleep(3)
        # 这里居然埋坑
        element4 = self.drvice.find_element_by_xpath("//input[@type='checkbox']/../input[4]")
        element4.click()
        sleep(3)

    def radio_dome(self):
        element1 = self.drvice.find_element_by_css_selector("input[value='rv1']")
        element2 = self.drvice.find_element_by_css_selector("input[value='rv2']")
        element1.click()
        print(element1.is_selected())
        print(element2.is_selected())
        sleep(3)

        element2.click()
        print(element1.is_selected())
        print(element2.is_selected())

    def password_dome(self):
        element1 = self.drvice.find_element_by_xpath("//input[@type='password' and @name='p1']")
        element1.clear()
        element1.send_keys("测试输入")
        sleep(3)
        element2 = self.drvice.find_element_by_xpath("//input[@type='password' and not(@name='p1')]")
        element2.clear()
        element2.send_keys("测试数据2")
        sleep(3)

    def select_dome1(self):
        element = self.drvice.find_element_by_xpath("//select[@name='s1']")
        element.click()
        element1 = self.drvice.find_element_by_xpath("//select[@name='s1']/option[@value='o1']")
        element2 = self.drvice.find_element_by_xpath("//select[@name='s1']/option[@value='o2']")
        element3 = self.drvice.find_element_by_xpath("//select[@name='s1']/option[@value='o3']")
        element1.click()
        self.drvice.switch_to.active_element.click()
        print(element1.is_selected())
        print(element2.is_selected())
        print(element3.is_selected())
        sleep(2)

        element.click()
        element2.click()
        self.drvice.switch_to.alert.accept()
        print(element1.is_selected())
        print(element2.is_selected())
        print(element3.is_selected())
        sleep(2)

        element.click()
        element3.click()
        self.drvice.switch_to.alert.accept()
        print(element1.is_selected())
        print(element2.is_selected())
        print(element3.is_selected())
        sleep(2)

    def select_dome2(self):
        element = self.drvice.find_element_by_xpath("//select[@id='s1Id' and not(@name='s1')]")
        element.click()
        element1 = self.drvice.find_element_by_xpath("//select[@id='s1Id' and not(@name='s1')]/option[@value='o1']")
        element2 = self.drvice.find_element_by_xpath("//select[@id='s1Id' and not(@name='s1')]/option[@value='o2']")
        element3 = self.drvice.find_element_by_xpath("//select[@id='s1Id' and not(@name='s1')]/option[@value='o3']")
        element1.click()
        self.drvice.switch_to.active_element.click()
        # self.drvice.switch_to.alert.accept()
        print(element1.is_selected())
        print(element2.is_selected())
        print(element3.is_selected())
        sleep(2)

        element.click()
        element2.click()
        self.drvice.switch_to.active_element.click()
        # self.drvice.switch_to.alert.accept()
        print(element1.is_selected())
        print(element2.is_selected())
        print(element3.is_selected())
        sleep(2)

        element.click()
        element3.click()
        # self.drvice.switch_to.alert.accept()
        self.drvice.switch_to.active_element.click()
        print(element1.is_selected())
        print(element2.is_selected())
        print(element3.is_selected())
        sleep(2)

    def select_dome3(self):
        element = self.drvice.find_element_by_xpath("//select[3]")
        element.click()
        element1 = self.drvice.find_element_by_xpath("//select[3]/option[@value='o1']")
        element2 = self.drvice.find_element_by_xpath("//select[3]/option[@value='o2']")
        element3 = self.drvice.find_element_by_xpath("//select[3]/option[@value='o3']")
        element1.click()
        self.drvice.switch_to.active_element.click()
        # self.drvice.switch_to.alert.accept()
        print(element1.is_selected())
        print(element2.is_selected())
        print(element3.is_selected())
        sleep(2)

        element.click()
        element2.click()
        self.drvice.switch_to.active_element.click()
        # self.drvice.switch_to.alert.accept()
        print(element1.is_selected())
        print(element2.is_selected())
        print(element3.is_selected())
        sleep(2)

        element.click()
        element3.click()
        # self.drvice.switch_to.alert.accept()
        self.drvice.switch_to.active_element.click()
        print(element1.is_selected())
        print(element2.is_selected())
        print(element3.is_selected())
        sleep(2)

    def select_dome4(self):
        element = self.drvice.find_element_by_xpath("//select[@multiple='multiple']")
        element1 = self.drvice.find_element_by_xpath("//select[@multiple='multiple']/option[1]")
        element2 = self.drvice.find_element_by_xpath("//select[@multiple='multiple']/option[2]")
        element3 = self.drvice.find_element_by_xpath("//select[@multiple='multiple']/option[3]")
        select_element = Select(element)
        select_element.select_by_value("o1")
        # self.drvice.switch_to.active_element.click()
        self.drvice.switch_to.alert.accept()
        select_element.select_by_value("o2")
        # self.drvice.switch_to.active_element.click()
        self.drvice.switch_to.alert.accept()
        select_element.select_by_value("o3")
        # self.drvice.switch_to.active_element.click()
        self.drvice.switch_to.alert.accept()
        print(element1.is_selected())
        print(element2.is_selected())
        print(element3.is_selected())

    def button_reset_demo1(self):
        element = self.drvice.find_element_by_xpath("//input[@name='resetTest']")
        element.clear()
        element.send_keys("test")
        element1 = self.drvice.find_element_by_xpath("//input[@id='resetId']")
        element1.click()
        print(element.text)
        element.clear()
        element.send_keys("test2")
        element2 = self.drvice.find_element_by_xpath("//input[@name='resetName' and not(@id='resetId')]")
        element2.click()
        print(element.text)
        element.clear()
        element.send_keys("test3")
        element3 = self.drvice.find_element_by_xpath("//input[@id='resetId1']")
        element3.click()
        print(element.text)
        element.clear()
        element.send_keys("test4")
        element2 = self.drvice.find_element_by_xpath("//input[@type='reset'][4]")
        element2.click()
        print(element.text)

    def Button_dome2(self):
        element1 = self.drvice.find_element_by_css_selector("#buttonId")
        element1.click()
        element2 = self.drvice.find_element_by_xpath("/html/body/form/button[2]")
        element2.click()


if __name__ == '__main__':
    formTest = FormTestDome()
    # 执行测试方法
    # formTest.input_name()
    # formTest.input_css_name2()
    # formTest.input_xpath()
    # formTest.input_css_attribute()
    # formTest.input_css_attribute2()
    # formTest.input_css_type()
    # formTest.input_css_type2()
    # formTest.textarea_input()
    # formTest.checkbox_dome()
    # formTest.radio_dome()
    # formTest.password_dome()
    # formTest.select_dome4()
    formTest.button_reset_demo1()
    formTest.quit()
