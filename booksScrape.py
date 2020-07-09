import time
import csv
import selenium
from selenium import webdriver

# DRIVER_PATH = 'C:\\Python\\chromedriver'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('http://books.toscrape.com/')

# goal: Loop through each page, store the name of the book and the price in a CSV file #
# Each page has 20 items and there are 50 pages. #

# booksAndPrices = open('booksAndPrices.csv', 'w')
# writer = csv.writer(booksAndPrices, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# writer.writerow(['testname', 'testprice'])
# booksAndPrices.flush()
# booksAndPrices.close()
with open('booksAndPrices.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows('someiterable')

    # for i in range(50):
    #     productsList = driver.find_element_by_xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol')
    #     products = productsList.find_elements_by_tag_name('li')
    #
    #     for product in products:
    #         productPrice = product.find_element_by_class_name('price_color').text
    #         print("Price :", productPrice)
    #
    #         productName = product.find_element_by_tag_name('h3')
    #         productName = productName.find_element_by_tag_name('a').get_attribute('title')
    #         print("Name :", productName)
    #
    #         booksAndPrices_writer.writerow([productName, productPrice])
    #
    #     nextPage = driver.find_element_by_class_name('next')
    #     nextPage = nextPage.find_element_by_tag_name('a')
    #     nextPage.click()
