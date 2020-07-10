import csv
import selenium
from selenium import webdriver

DRIVER_PATH = 'C:\\Python\\chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('http://quotes.toscrape.com/')

# goal: Loop through each quote, store the name of the AUTHOR and the QUOTE in a CSV file #
count=0
with open('C:\\Users\\Rebecca\\github\\booksScrape\\quotesAndAuthors.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Author', 'Quote'])

    for i in range(10):
        quotesList = driver.find_elements_by_class_name('quote')

        for quoteObj in quotesList:
            quote = quoteObj.find_element_by_class_name('text').text
            author = quoteObj.find_element_by_class_name('author').text
            if "′" in quote:
                quote = quote.replace("′", "'")

            writer.writerow([author, quote])

            count+=1
            print('Quotes collected :', count)

        if i < 9:
            next = driver.find_element_by_class_name('next').find_element_by_tag_name('a')
            next.click()
            print('yo we onto the next page ayyy')
