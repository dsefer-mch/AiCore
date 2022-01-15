from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, os
from time import sleep



retailers_url = ['https://www.sainsburys.co.uk/']#['https://www.asda.com/','https://www.tesco.com/', 'https://groceries.morrisons.com/webshop/startWebshop.do', 'https://www.lidl.co.uk/', 'https://www.aldi.co.uk/', 'https://www.sainsburys.co.uk/']
list_groceries = ['lemons', 'cucumbers', 'chicken brests', 'yorkshire tea']

# chrome = webdriver.Chrome()
# for retailer in retailers_url:
#     # Path where you want to save/load cookies to/from 
#     cookies_location = f"/home/mch/AiCore/GitHub/AiCore/Python/cookies_{retailer.split('.')[1]}.txt" ### !!need to provide absol path on this one
#     chrome.get(retailer)
#     cookies.save_cookies(chrome, cookies_location)
# chrome.quit()

driver = webdriver.Chrome()

for retailer in retailers_url:
    cookies_location = f"/home/mch/AiCore/GitHub/AiCore/Python/cookies_{retailer.split('.')[1]}.txt"
    driver.get(retailer)
    driver.maximize_window()
    sleep(80)
    search = driver.find_element_by_xpath("//INPUT[@id='term']")
    search.send_keys('lemons')
    search.send_keys(Keys.RETURN)

    # filter = driver.find_element_by_xpath("//SELECT[@id='product-controls-sort-dropdown']").click()
    # low_price = driver.find_element_by_link_text('Price - Low to High').click()
    # item = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='app ']/div[@class='ln-o-page']/div[@class='ln-o-page__body']/div[@class='ln-o-container ln-o-container--soft padding-bottom-default']/div/section[@class='ln-o-section margin-top-default']/div[@class='SRF']/div[@class='SRF__tileList']/ul[@class='ln-o-grid ln-o-grid--matrix ln-o-grid--equal-height']/li[@class='pt-grid-item ln-o-grid__item ln-u-1/2@xs ln-u-1/4@md ln-u-1/5@xl'][2]/div[@class='ln-c-card pt']/div[@class='pt__content']/div[@class='pt__wrapper']/div[@class='pt__wrapper-inner']").text
    # print(item)
sleep(50)
driver.quit()