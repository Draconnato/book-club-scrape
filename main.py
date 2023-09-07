import script.scraper as scraper
import pyarrow.parquet as pq
import pyarrow as pa

URL = "https://books.toscrape.com/"

chrome = scraper.launchChrome() #start selenium

page = scraper.getSourcePage(chrome,URL) #get a page content from a source page - required

categoryURL = scraper.getCategoryList(page) # get a category list and URL - required

for i in categoryURL:
    currentCategory = categoryURL[i]
    book = scraper.scrapePage(chrome,URL+currentCategory)

    book_test = pa.Table.from_pylist(book)

    pq.write_table(book_test,'files/'+i+'.parquet')

# need to fix the filenames and works with dataset (partition files: https://arrow.apache.org/docs/python/parquet.html#reading-from-partitioned-datasets)