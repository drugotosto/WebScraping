from BasicScraping.basic import startScraping
from BasicScraping.getLinks import getAllExternalLinks
from Cleaning.cleanInput import pulisciTesto
from CookieSession.loginManage import login
from SeleniumManage.basic import recuperoDati,apriFirefox,cerca
from SeleniumManage.redirectJavascript import waitForLoad
from AvoidTraps.seleniumCookies import cookieManage
from retriveDatiTrip import retriveRestaurants

if __name__ == '__main__':

    # startScraping("http://www.pythonscraping.com/pages/page3.html")

    """Recupero di tutti i link esterni di una data pagina (BeautifulSoup)"""
    # listaLinkEsterni=getAllExternalLinks("http://oreilly.com")

    """Una volta pulito il testo ne esegue una suddivisione in n_grams per poi calcolarne il numero totale (BeautifulSoup)"""
    # pulisciTesto()

    """Login alla pagina con memorizzazione dei cookie da utilizzare successicamente per altre pagine (requests.Session())"""
    # login()

    """Apre Firefox e carica una pagina (Selenium)"""
    # apriFirefox()

    """Ricerca in Google con stampa a video dei link del contenuto e su files (html/png) della pagina risultante dalla ricerca fatta (Selenium,Phantomjs)"""
    # cerca()

    """Stampa testo di una pagina solo dopo la comparsa di un dato elemento"""
    # recuperoDati()

    """Gestione di una redirezione tramite Javascript"""
    # waitForLoad()

    "Gestione dei Cookies con Selenium"
    # cookieManage()

    retriveRestaurants("torino",1,"drugotosto@libero.it","UfhA2ybn")