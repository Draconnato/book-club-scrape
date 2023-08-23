from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup, NavigableString
from pprint import pprint


URL = "https://books.toscrape.com/"

chromeOptions = Options()

chromeOptions.add_argument("--headless")

driver = webdriver.Chrome(options=chromeOptions)

driver.implicitly_wait(10)

def getSourcePage(url):

    driver.get(url)

    source = driver.page_source

    return source
    
#page = getSourcePage(url=URL)

def getCategoryList(pageHtml):

    soup = BeautifulSoup(pageHtml,'html.parser')

    categoryList = {}

    for listClass in soup.find_all('ul',class_="nav nav-list"):
        for list in listClass.find_all('li'):

            if isinstance(list,NavigableString):
                continue
            else:
                for childrenList in list.find_all('ul'):
                    for newChildrenList in childrenList.find_all('li'):
                        categoryList.update({newChildrenList.a.text.strip():newChildrenList.a['href'].strip()})
    
    driver.quit

    return categoryList