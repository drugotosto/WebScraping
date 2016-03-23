from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def retriveRestaurants(location,maxPag,userEmail,password):
    browser= webdriver.Firefox()
    browser.get("http://tripadvisor.com")
    browser.maximize_window()
    # browserAlt.implicitly_wait(1)

    browser.find_element_by_xpath("//a[contains(text(), 'I tuoi amici')]").click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "FBC_LOGIN"))).click()

    main_window_handle = browser.current_window_handle
    signin_window_handle = None
    while not signin_window_handle:
        for handle in browser.window_handles:
            if handle != main_window_handle:
                signin_window_handle = handle
                break

    browser.switch_to.window(signin_window_handle)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(userEmail)
    browser.find_element_by_id('pass').send_keys(password)
    browser.find_element_by_xpath("//input[@value='Accedi']").click()
    browser.switch_to.window(main_window_handle)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "mainSearch"))).send_keys(location)
    browser.find_element_by_id('SEARCH_BUTTON').click()
    browser.find_element_by_xpath("//span[@title='Ristoranti']").click()
    numPag=0
    while(browser.find_element_by_xpath("//span[contains(text(), 'Successivo')]").is_enabled())and(numPag<maxPag):
        print("\n\nPAGINA",numPag)
        listaDivRistoranti=browser.find_elements_by_xpath("//div[@class='result EATERY']")
        for divRistorante in listaDivRistoranti:
            print("\nDIV:",divRistorante.text)
        browser.find_element_by_xpath("//span[text()='Successivo']").click()
        numPag+=1
