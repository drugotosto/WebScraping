import requests

def login():
    session = requests.Session()

    params = {'username': 'username', 'password': 'password'}
    s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
    print("Cookie is set to:")
    print(s.cookies.get_dict())
    print("-----------")
    print("Going to profile page...")
    s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
    print(s.text)

    """savedCookies=browserAlt.get_cookies()

    browser=webdriver.PhantomJS()
    browser.delete_all_cookies()
    for cookie in savedCookies:
        browser.add_cookie(cookie)

    browser.get("http://tripadvisor.com")
    # browser.implicitly_wait(1)
    # print("\n\nCookies recuperati tramite Phantom:",browser.get_cookies())
    # print("Differenza:",[x for x in browserAlt.get_cookies() if x not in browser.get_cookies()])"""