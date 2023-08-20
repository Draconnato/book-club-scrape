from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup, NavigableString

URL = "https://books.toscrape.com/"

chromeOptions = Options()

chromeOptions.add_argument("--headless")

driver = webdriver.Chrome(options=chromeOptions)

driver.implicitly_wait(10)

def getSourcePage(url):

    driver.get(url)

    source = driver.page_source

    return source
    
page = getSourcePage(url=URL)

soup = BeautifulSoup(page,'html.parser')


for listClass in soup.find_all('ul',class_="nav nav-list"):
    for list in listClass.find_all('li'):
        
        if isinstance(list,NavigableString):
            continue
        else:
            for childrenList in list.find_all('ul'):
                for novaChildrenList in childrenList.find_all('li'):
                    print(novaChildrenList.a.text.strip())




driver.quit