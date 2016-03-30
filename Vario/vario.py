_author__ = 'maury'
from BeautifulSoup import BeautifulSoup
import os
import requests


def filtraReviews():
    form={"returnTo":"__2F__Attraction__5F__Review__2D__g187855__2D__d264480__2D__Reviews__2D__Museo__5F__Nazionale__5F__del__5F__Cinema__2D__Turin__5F__Province__5F__of__5F__Turin__5F__Piedmont__2E__html#REVIEWS","filterSegment":"5","mode":"filterReviews","filterLang":"en","t":"no lift","askForConfirmation":"false"}
    url="https://www.tripadvisor.com/Attraction_Review-g187855-d264480-Reviews-Museo_Nazionale_del_Cinema-Turin_Province_of_Turin_Piedmont.html"
    # headers={'content-type':'application/x-www-form-urlencoded'}
    r=requests.post(url,data=form)
    soup=BeautifulSoup(r.content)
    with open("data/reviews.html", 'wb') as fp:
        fp.write(soup.prettify())

def recupero_URL_utente():
    url="https://www.tripadvisor.com/MemberOverlay?uid=DD516B2EEAB8564BB81EDAB7A7BA21A3&c=&src=303266724&fus=false&partner=false&LsoId="
    r=requests.get(url)
    soup=BeautifulSoup(r.content)
    with open("data/profiloUtente.html", 'wb') as fp:
        fp.write(soup.prettify())

if __name__ == '__main__':
    os.makedirs("data")
    filtraReviews()
    recupero_URL_utente()