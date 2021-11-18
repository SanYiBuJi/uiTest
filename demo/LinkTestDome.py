# -*- coding:utf-8 -*-
# Author : SanYiBuJi
# Data : 2022/3/1 23:29
from time import sleep

from selenium import webdriver


class LinkTestDome:
    def __init__(self):
        self.drvice = webdriver.Chrome("D:\\Tools\\WebDriver\\chromedriver.exe")
        self.drvice.get("http://sahitest.com/demo/linkTest.htm")

    def linkByContentDome(self):
        self.drvice.find_element_by_link_text("linkByContent").click()
        sleep(3)


if __name__ == '__main__':
    linktestdome = LinkTestDome()
    linktestdome.linkByContentDome()