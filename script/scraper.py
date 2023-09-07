from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup, NavigableString
import json
import re


def launchChrome(visibility=0):
    
    chromeOptions = Options()
    chromeOptions.add_argument('log-level=3') #supress to get only fatal erros in a prompt

    if visibility == 0:
        chromeOptions.add_argument('--headless') # chrome tab will be hide
        driver = webdriver.Chrome(options=chromeOptions)
    else: 
        driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    return driver

def getSourcePage(driver,url):

    driver.get(url)

    source = driver.page_source

    return source

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
                        category = newChildrenList.a.text.strip()
                        link = newChildrenList.a['href'].strip()[:-10]
                        categoryList.update({category:link})

    return categoryList

def getBookData(pageContent):

    books = [] # List of books

    soup = BeautifulSoup(pageContent,'html.parser')

    for table in soup.find_all('ol',class_='row'):

        for book in table('li'):

            title = book.h3.a['title'].strip()
            value = book.find('p',class_='price_color').string
            availability = book.find('p',class_='instock availability').text.strip()
            rating = book.find('p',class_=re.compile('^star-rating'))['class'][1] 
            imageURL = book.find('img')['src']

            bookContent = {
                'title': title
                ,'value': value
                ,'availability': availability
                ,'rating': rating
                ,'imageURL': imageURL
            }

            books.append(bookContent)

    return books#json.dumps(books,ensure_ascii=False)# ensure_ascii=False Fix the currency code

def hasNextPage(pageContent):

    soup = BeautifulSoup(pageContent,'html.parser')
    
    nextButton = soup.find_all('li',class_='next')

    if len(nextButton) > 0:
        nextButton = nextButton[0].a['href']

    return nextButton

def scrapePage(chrome,URL):

    sourcePage = getSourcePage(chrome,URL)

    nextPage = hasNextPage(sourcePage)

    bookData = getBookData(sourcePage)

    while len(nextPage) > 0:

        sourcePage = getSourcePage(chrome,URL+nextPage)

        nextPage = hasNextPage(sourcePage)

        bookData.extend(getBookData(sourcePage))

    return bookData#json.dumps(bookData)
        