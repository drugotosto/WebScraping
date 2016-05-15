from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchWindowException, \
    NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

_author__ = 'maury'

from BeautifulSoup import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
from Vario.headLessBrowser import HeadLessBrowswer

def filtraReviews():
    form={"returnTo":"__2F__Attraction__5F__Review__2D__g187855__2D__d1916474__2D__Reviews__2D__or10__2D__Mercato__5F__di__5F__Porta__5F__Palazzo__2D__Turin__5F__Province__5F__of__5F__Turin__5F__Piedmont__2E__html#REVIEWS","mode":"filterReviews","filterLang":"en","filterSegment":2}
    url="https://www.tripadvisor.com/Attraction_Review-g187855-d1916474-Reviews-or10-Mercato_di_Porta_Palazzo-Turin_Province_of_Turin_Piedmont.html#REVIEWS"
    # headers={'content-type':'application/x-www-form-urlencoded'}
    r=requests.post(url,data=form)
    soup=BeautifulSoup(r.content)
    with open("data/reviews.html", 'wb') as fp:
        fp.write(soup.prettify())


def recupero_URL_utente():
    url="https://www.tripadvisor.com/MemberOverlay?uid=DD516B2EEAB8564BB81EDAB7A7BA21A3 & c= & src=303266724 & fus=false & partner=false & LsoId="
    r=requests.get(url)
    soup=BeautifulSoup(r.content)
    with open("data/profiloUtente.html", 'wb') as fp:
        fp.write(soup.prettify())

def retriveRatings(browser,mainWind,url):
    browser.driver.get(url)
    windows=browser.driver.window_handles
    for wind in windows:
        if wind!=mainWind:
            browser.driver.switch_to_window(wind)
            browser.driver.close()

    browser.driver.switch_to_window(mainWind)

    # Azioni per andare a chiudere il popup nel caso apparisse
    actions = ActionChains(browser.driver)
    actions.move_by_offset(40,50).click()
    actions.perform()

    # Filtraggio dei Rates per RATINGS e ATTRAZIONI
    try:
        ratesFilter=browser.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.cs-contribution-bar > li[data-filter='RATINGS_ALL'] > a")))
        ratesFilter.click()

    except TimeoutException:
        print "\n\nNon e presente il filtro per RATINGS!"
        return
    try:
        dataFilter=browser.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.cs-filter-bar ul > li[data-filter='RATINGS_ATTRACTIONS']")))
        dataFilter.click()
    except TimeoutException:
        print "\n\nNon e presente il filtro per ATTRACTIONS!"
        return

    # Recupero dei dati dei vari RATES
    nextPage,globDates,globLocations,globAttractions,globRates=True,[],[],[],[]
    while nextPage:
        try:
            dates=browser.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cs-rating-date")))
            locations=browser.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cs-rating-geo")))
            attractions=browser.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cs-rating-location a")))
            rates=browser.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cs-rating img")))

            dates=[date.text for date in dates]
            locations=[loc.text for loc in locations]
            attractions=[attr.text for attr in attractions]
            rates=[rate.get_attribute("content") for rate in rates]

            print "\n\nATTRAZIONI: {}\n\nLOCATIONS: {}\n\nRATES: {}\n\nDATES: {}".format(attractions,locations,rates,dates)
            globDates.extend(dates)
            globLocations.extend(locations)
            globAttractions.extend(attractions)
            globRates.extend(rates)

        except TimeoutException:
            print "\nTempo Terminato! Elementi non trovati"
        try:
            nextPage=browser.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#cs-paginate-next")))
            actions=ActionChains(browser.driver)
            actions.click(nextPage)
            actions.perform()

        except WebDriverException:
            print "\nNEXT non presente!"
            nextPage=None

    return zip(globDates,globLocations,globAttractions,globRates)


if __name__ == '__main__':
    # os.makedirs("data")
    # filtraReviews()
    # recupero_URL_utente()
    browser=HeadLessBrowswer()
    browser.driver.maximize_window()
    mainWind=browser.driver.current_window_handle
    # "https://www.tripadvisor.com/members/616sarap","https://www.tripadvisor.com/members/Luca-Reset","https://www.tripadvisor.com/members/euklitb"
    urls=["https://www.tripadvisor.com/members/chrviddmquat"]
    info=None
    for url in urls:
        print "\n\nPAGINA: {}".format(url)
        info=retriveRatings(browser,mainWind,url)

    browser.driver.close()
    print "\n\nINFO: {} LEN: {}".format(str(info),len(info))
    keys=("date","location","attraction","rate")
    rating=[dict(zip(keys,val)) for val in info]
    print "\n\nRATINGS: {}  LEN: {}".format(rating,len(rating))