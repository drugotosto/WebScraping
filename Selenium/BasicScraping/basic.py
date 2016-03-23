from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

def startScraping(url):
    print("\n**********Esempio di Scraping base...")
    try:
        html = urlopen(url)
    except HTTPError as e:
        result="Pagina non trovata sul server"
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        result = bsObj.find("tr",{"id":"gift1"}).attrs
    except AttributeError as e:
        result="Il Server non e stato trovato on e presente il tag cercato!"

    print("Risultato:",result)