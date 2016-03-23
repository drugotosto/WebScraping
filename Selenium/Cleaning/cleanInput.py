from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import string

def pulisciTesto():
    html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
    bsObj = BeautifulSoup(html.read(),"html.parser")
    content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
    ngrams = ngramsFunc(content, 2)
    print(ngrams)
    print("2-grams count is: "+str(len(ngrams)))

def cleanInput(testo):
    testo = re.sub('\n+', " ", testo)
    testo = re.sub('\[[0-9]*\]', "", testo)
    testo = re.sub(' +', " ", testo)
    testo = bytes(testo, "UTF-8")
    testo = testo.decode("ascii", "ignore")
    cleanInput = []
    testo = testo.split(' ')
    for item in testo:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngramsFunc(testo, n):
    input_file = open("C:\\Users\\drugo\\PycharmProjects\\WebScraping\\Cleaning\\testoInput.txt","w")
    testo = bytes(testo, "UTF-8")
    testo=testo.decode("ascii","ignore")
    input_file.write(testo)
    input_file.close()

    testo = cleanInput(testo)

    output_file = open("C:\\Users\\drugo\\PycharmProjects\\WebScraping\\Cleaning\\testoOutput.txt","w")
    output_file.write(str(testo))
    output_file.close()

    output = []
    for i in range(len(testo)-n+1):
        output.append(testo[i:i+n])
    return output

