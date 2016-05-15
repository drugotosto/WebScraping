__author__ = 'maury'

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class HeadLessBrowswer:
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.wait=WebDriverWait(self.driver,3)