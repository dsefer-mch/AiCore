from ast import Div
from asyncio import futures
from logging import exception
from urllib.request import Request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.skyscanner.net/")
# driver.implicitly_wait(10)
sleep(5)

try:
    print('zapo4vam')
    url = str("'" + driver.current_url + "'")
    print(url)
    r = requests.get(url)
    print(r)
    soup = bs(r.content)
    contents = soup.prettify()
    print(contents)
    all_ids = []
    all_ids = re.findall("id=.*", soup)
    print('id are: ', all_ids)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element_by_xpath(
        "/html/body/div/div/div[2]/div[2]/p")).click_and_hold()
    print(driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/p"))
    print('dobre li e?')
except:
    print('We are all humans')


try:
    driver.find_element(By.ID, "acceptCookieButton").click()
except:
    print("No cookies!Great...")
try:
    from_dest = driver.find_element(By.XPATH, "//*[@id='fsc-origin-search']")
    from_dest.send_keys('london')
    to_dest = driver.find_element(
        By.XPATH, "//*[@id='fsc-destination-search']")
    to_dest.send_keys('paris')

    driver.find_element(
        By.XPATH, "//*[@id='depart-fsc-datepicker-button']").click()
    # date_of_dep = driver.find_element(By.TAG_NAME, 'span aria-hidden="true"')
    # print(date_of_dep)
except:
    driver.delete_all_cookies()


# action = ActionChains(driver)
# driver.move_to_element(driver.find_element_by_xpath("//*[@id='depart-fsc-datepicker-popover'']/div/div/div[1]/div/nav/div/div[2]/button")).click()
# action.perform()
# action.move_to_element(driver.find_element_by_xpath('//*[@id="depart-fsc-datepicker-popover"]/div/div/div[1]/div/nav/div/div[2]/button')).click()
# action.perform()
# action.move_to_element(driver.find_element_by_link_text('June')).click()
# action.perform()
# driver.find_element_by_xpath("//*[@id='return-fsc-datepicker-button']").click()


# action.move_to_element(driver.find_element_by_link_text('Whole month')).click()
# action.perform()
# action.move_to_element(driver.find_element_by_link_text('June')).click()
# action.perform()

# driver.find_element_by_xpath("//*[@id='CabinClassTravellersSelector_fsc-class-travellers-trigger__OTYyM']").click()
# action.perform()
# driver.find_element_by_xpath("//*[@id='cabin-class-travellers-popover']/div/div/div[2]/div/button[2]").click()
# action.perform()
# driver.move_to_element(driver.find_element_by_link_text('Done')).click()
# action.perform()

# driver.move_to_element(driver.find_element_by_link_text('Search flights')).click()
# action.perform()


# action.perform()
# action.move_to_element(driver.find_element_by_xpath("//span[text()='Items']"))
# action.perform()
# action.move_to_element(driver.find_element_by_link_text('Weapons'))
# action.perform()
# driver.find_element_by_link_text('Daggers').click()


# num_of_items = int(driver.find_element_by_xpath('//*[@class="listview-note"]').text.split()[0])

# filter_min_lvl = driver.find_element_by_name('minle')
# filter_max_lvl = driver.find_element_by_name('maxle')
# filter_max_lvl.send_keys('270')
# filter_min_lvl.send_keys('213')
# filter_max_lvl.send_keys(Keys.RETURN)

# num_of_row = int(driver.find_element_by_xpath('//*[@class="listview-nav"]').text.split()[2])
driver.delete_all_cookies()
driver.implicitly_wait(100)
driver.quit()
