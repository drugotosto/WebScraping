from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def recuperoDati():
    driver = webdriver.PhantomJS()
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
    finally:
        print(driver.find_element_by_id("content").text)
        driver.close()

def apriFirefox():
    browser = webdriver.Firefox()
    browser.get('http://seleniumhq.org/')

def cerca():
    browser = webdriver.PhantomJS()
    browser.get('http://www.google.com')
    elem = browser.find_element_by_name('q')  # Find the search box
    elem.send_keys('seleniumhq' + Keys.RETURN)
    browser.get_screenshot_as_file("cerca.png")
    output_file = open("cerca.html","w")
    output_file.write(browser.page_source.encode('utf-8').strip())
    output_file.close()
    print("CONTEUNUTO PAGINA:",browser.find_element_by_tag_name("body").text)
    """Stampa dei vari link (non nulli) con relativo testo associato"""
    links=browser.find_elements_by_xpath("//div[@id='res']//a[@href]")
    links=[link for link in links if link.text!=""]
    for link in links:
        print("\nTesto Link:",link.text)


