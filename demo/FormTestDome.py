# -*- coding:utf-8 -*-
# Author : SanYiBuJi
# Data : 2022/3/13 22:51
from selenium import webdriver
from time import sleep

class FormTestDome:
    '''
    测试http://sahitest.com/demo/formTest.htm 中的元素定位练习
    Test the elements in the http://sahitest.com/demo/formTest.htm location practice
    '''

    TestURl = "http://sahitest.com/demo/formTest.htm"
    def __init__(self):
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
    formTest.quit()