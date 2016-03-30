__author__ = 'maury'
import robotparser

def verifica():
    """
    Verifica la possibilita da parte dello scraper di eseguire accedere a determinati url
    """
    rp=robotparser.RobotFileParser()
    rp.set_url("https://www.tripadvisor.com/robots.txt")
    rp.read()
    url= "https://www.tripadvisor.com/Attractions-g1152935-Activities-c47-Province_of_Turin_Piedmont.html#ATTRACTION_LIST"
    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
    return rp.can_fetch(user_agent,url)


if __name__ == '__main__':
    print("Risposta: {}".format(verifica()))
