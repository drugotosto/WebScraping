from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

def waitForLoad():
    driver = webdriver.PhantomJS()
    driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")

    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning\n\n")
            print(driver.page_source)
            return
        time.sleep(.5)
        try:
            elem = driver.find_element_by_xpath("//div[@id='content']")
            print("\n\n",driver.page_source)
        except NoSuchElementException:
            print("\n\nHo avuto una redirizione!\n\n")
            print(driver.page_source)
            return
