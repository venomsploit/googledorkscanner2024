#GOOGLE DORK SCANNER WITH ZONE H GRABBER
from selenium import webdriver
from re import findall
from requests import session

def GoogleEngineDork(dork, pagesX):
    pages = []
    domains = []
    i = 0
    pp = pagesX * 10
    while i <= pp:
        pages.append(str(i))
        i += 10

    with webdriver.Chrome() as browser:
        for page in pages:
            browser.get('https://www.google.com/search?q={}&start={}'.format(dork, page))
            try:
                if ".style.display='block'" in str(browser.page_source):
                    input('Captcha Detected! answer to Captcha and press ENTER to continue...')
                    browser.get('https://www.google.com/search?q={}&start={}'.format(dork, page))
                    urls = findall('://([A-Za-z_0-9.-]+).', browser.page_source)
                    for url in list(set(urls)):
                        if 'google.' in url or 'schema.org' in url or 'googleusercontent' in url or '.w3.org' in url or 'gstatic.' in url or 'languages.oup.com' in url or 'en.wikipedia.org' in url:
                            pass
                        else:
                            if url.startswith('http://'):
                                url = url.replace('http://', '')
                            elif url.startswith("https://"):
                                url = url.replace('https://', '')
                            else:
                                pass
                            domains.append(url)
                            print(url)
                else:
                    urls = findall('://([A-Za-z_0-9.-]+).', browser.page_source)
                    for url in list(set(urls)):
                        if 'google.' in url or 'schema.org' in url or 'googleusercontent' in url or '.w3.org' in url or 'gstatic.' in url or 'languages.oup.com' in url or 'en.wikipedia.org' in url:
                            pass
                        else:
                            if url.startswith('http://'):
                                url = url.replace('http://', '')
                            elif url.startswith("https://"):
                                url = url.replace('https://', '')
                            else:
                                pass
                            domains.append(url)
                            print(url)
            except:
                pass
    return list(set(domains))

def Googledorker(dork, pages):
    Engine = GoogleEngineDork(dork, pages)
    print(Engine)
    if len(Engine) != 0:
        for url in Engine:
            open('GrabbedSites_GoogleDork.txt', 'a').write(url + '\n')


def GET_CVID(sess):
    try:
        cnn = sess.get('https://www.bing.com/', timeout=5)
        CVID = findall('</a><span id="nc_iid" _IG="(.*)"', cnn.text)[0].split('"')[0]
        Code = findall('"IsChromeExtensionUser":false,"FormCode":"(.*)",', cnn.text)[0].split('"')[0]
        return CVID, Code
    except:
        return 'ERROR'

def EngineDork(dork, Cvid, Code, pagesX):
    pages = []
    domains = []
    i = 0
    pp = pagesX * 50
    while i <= pp:
        pages.append(str(i))
        i += 50
    with webdriver.Chrome() as browser:
        for page in pages:
            browser.get('https://www.bing.com/search?q={}&form={}&sp=-1&pq={}&qs=n&sk=&cvid={}&count=50&first={}'.format(dork, Code, dork, Cvid, page))
            try:
                matches = findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', browser.page_source)
                for url in matches:
                    if '/' in url:
                        if str(url).startswith('http://'):
                            url = str(url).replace('http://', '')
                        if str(url).startswith('https://'):
                            url = str(url).replace('https://', '')

                        url = url.split('/')[0]
                        if 'bing.' in url or 'w3.' in url:
                            pass
                        else:
                            if url not in domains:
                                domains.append(url)
                                print(url)
                            else:
                                pass
            except:
                pass
    return list(set(domains))

def dorker(dork, pages):
    sess = session()
    CVID, Code = GET_CVID(sess)
    if CVID == 'ERROR':
        print('We cant GET Code, CVID from Bing.com! Maybe your IP address Blocked By The Server!')
    else:
        Engine = EngineDork(dork, CVID, Code, pages)
        print(Engine)
        if len(Engine) != 0:
            for url in Engine:
                open('GrabbedSites_bingDork.txt', 'a').write(url + '\n')



def EngineH(notifier, pagesX):
    pages = []
    domains = []
    i = 1
    if pagesX == 1:
        pages.append(str(1))
    else:
        while i <= pagesX:
            pages.append(str(i))
            i += 1

    with webdriver.Chrome() as browser:
        for page in pages:
            browser.get('http://www.zone-h.org/archive/notifier={}/page={}'.format(notifier, page))
            try:
                if 'name="captcha"' in str(browser.page_source):
                    input('Captcha Detected! answer to Captcha and press ENTER to continue...')
                    browser.get('http://www.zone-h.org/archive/notifier={}/page={}'.format(notifier, page))
                    urls = findall('<td>(.*)\n							</td>', str(browser.page_source))
                    for url in list(set(urls)):
                        if url.startswith('http://'):
                            url = url.replace('http://', '')
                        elif url.startswith("https://"):
                            url = url.replace('https://', '')
                        else:
                            pass
                        domains.append(url)
                        print(url)
                else:
                    urls = findall('<td>(.*)\n							</td>', str(browser.page_source))
                    for url in list(set(urls)):
                        if url.startswith('http://'):
                            url = url.replace('http://', '')
                        elif url.startswith("https://"):
                            url = url.replace('https://', '')
                        else:
                            pass
                        domains.append(url)
                        print(url)
            except:
                pass
    return list(set(domains))

def EngineH2(notifier, pagesX):
    pages = []
    domains = []
    i = 1
    if pagesX == 1:
        pages.append(str(1))
    else:
        while i <= pagesX:
            pages.append(str(i))
            i += 1

    with webdriver.Chrome() as browser:
        for page in pages:
            url = 'https://www.zone-h.org/archive/filter=1/published=0/domain={}/fulltext=1/page={}'.format(notifier, page)
            browser.get(url)
            try:
                if 'name="captcha"' in str(browser.page_source):
                    input('Captcha Detected! Answer the Captcha and press ENTER to continue...')
                    browser.get(url)
                    urls = findall('<td>(.*)\n							</td>', str(browser.page_source))
                    for url in list(set(urls)):
                        if url.startswith('http://'):
                            url = url.replace('http://', '')
                        elif url.startswith("https://"):
                            url = url.replace('https://', '')
                        else:
                            pass
                        domains.append(url)
                        print(url)
                else:
                    urls = findall('<td>(.*)\n							</td>', str(browser.page_source))
                    for url in list(set(urls)):
                        if url.startswith('http://'):
                            url = url.replace('http://', '')
                        elif url.startswith("https://"):
                            url = url.replace('https://', '')
                        else:
                            pass
                        domains.append(url)
                        print(url)
            except Exception as e:
                print(f"Error: {e}")
    return list(set(domains))
    
def ZoneH(notifier, pages):
    Engine = EngineH(notifier, pages)
    print(Engine)
    if len(Engine) != 0:
        for url in Engine:
            if '/' in str(url):
                url = str(url).split('/')[0]
            open('GrabbedSites_Zone-h.org.txt', 'a').write(url + '\n')

def ZoneH2(notifier, pages):
    Engine = EngineH2(notifier, pages)
    print(Engine)
    if len(Engine) != 0:
        for url in Engine:
            if '/' in str(url):
                url = str(url).split('/')[0]
            open('GrabbedSites_Zone-h.org.txt', 'a').write(url + '\n')



print('-------------DOMAIN GRABBER @v3t4l1 -------------------')
print('1= bing.com Scanner')
print('2= Google.com Scanner')
print('3= Zone-H.org Scanner')
print('4= Zone-H.org Scanner/ TLD')
print('---------------------------------------------')
selector = input(' [Engine-Selector]: ')
if selector == str(1):
    dork = input(' [Bing.com] Dork: ')
    pages = int(input(' [Bing.com] page { How much pages you want get? }: '))
    dorker(dork, pages)
elif selector == str(2):
    dork = input(' [Google.com] Dork: ')
    pages = int(input(' [Google.com] page { How much pages you want get? }: '))
    Googledorker(dork, pages)
elif selector == str(3):
    Notifier = input(' [zone-h.org] Notifier: ')
    pages = int(input(' [zone-h.org] page { How much pages you want get? }: '))
    ZoneH(Notifier, pages)
elif selector == str(4):
    Notifier = input(' [zone-h.org] TLD: ')
    pages = int(input(' [zone-h.org] page { How much pages you want get? }: '))
    ZoneH2(Notifier, pages)
