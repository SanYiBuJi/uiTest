# -*- coding:utf-8 -*-
# Author : SanYiBuJi
# Data : 2022/3/1 23:29
from time import sleep

from selenium import webdriver


class LinkTestDome:
    '''
    测试http://sahitest.com/demo/linkTest.htm 中的元素定位练习
    Test the elements in the http://sahitest.com/demo/linkTest.htm location practice
    '''

    TestURL = "http://sahitest.com/demo/linkTest.htm"
    def __init__(self):
        self.drvice = webdriver.Chrome("D:\\Tools\\WebDriver\\chromedriver.exe")
        self.drvice.get(LinkTestDome.TestURL)

    def quit(self):
        self.drvice.quit()

    def linkByContentDome(self):
        self.drvice.find_element_by_link_text("linkByContent").click()
        sleep(3)


if __name__ == '__main__':
    linktestdome = LinkTestDome()
    linktestdome.linkByContentDome()
    linktestdome.quit()