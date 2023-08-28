import script.scraper as scraper

URL = "https://books.toscrape.com/"

chrome = scraper.launchChrome(visibility=1) #start selenium

page = scraper.getSourcePage(chrome,URL) #get a page content from a source page - required

#categoryURL = scraper.getCategoryList(page) # get a category list and URL - optional

#BookData = scraper.getBookData(page) # receive a json with data from all books in a page - optional


"""
for i in categoryURL:

    currentCategoryURL = categoryURL[i]

    pageContent = getSourcePage(URL+currentCategoryURL)  
    """