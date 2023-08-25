from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup, NavigableString

import re
import time

"""
Problem to be solve in the future:
The statements to run or quit the browser are inside of a function that shouldn't have this functionality, find a way to create a sub function or 
understand if this are a typical usecase from class
"""

URL = "https://books.toscrape.com/"

chromeOptions = Options()

chromeOptions.add_argument("--headless")

#driver = webdriver.Chrome(options=chromeOptions)
driver = webdriver.Chrome()


driver.implicitly_wait(10)

def getSourcePage(url):

    driver.get(url)

    source = driver.page_source

    return source
    
page = getSourcePage(url=URL)

def getCategoryList(pageHtml):

    categoryList = {}

    soup = BeautifulSoup(pageHtml,'html.parser')

    for listClass in soup.find_all('ul',class_="nav nav-list"):
        for list in listClass.find_all('li'):

            if isinstance(list,NavigableString):
                continue
            else:
                for childrenList in list.find_all('ul'):
                    for newChildrenList in childrenList.find_all('li'):
                        categoryList.update({newChildrenList.a.text.strip():newChildrenList.a['href'].strip()})
    
    #driver.quit

    return categoryList

categoryURL = getCategoryList(page)

def getData(pageContent):

    soup = BeautifulSoup(pageContent,'html.parser')

    for i in soup.find_all('ol',class_='row'):
        for j in i('li'):
            
            print(j)
            #print(j.h3.a['title']) # Book_Title
            #print(j.find('p',class_="price_color").string) #Book_Value
            #print(j.find('p',class_='instock availability').text.strip()) #Book_availability
            #print(j.find('p',class_=re.compile("^star-rating"))['class'][1]) #Book_stars
            #print(j.find('img')['src']) #book_image (needs concatenate with site URL)

getData(page)

"""
for i in categoryURL:

    currentCategoryURL = categoryURL[i]

    pageContent = getSourcePage(URL+currentCategoryURL)  
    """