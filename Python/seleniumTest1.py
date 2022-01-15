
# import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import re
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://wotlkdb.com/")
driver.maximize_window()
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_link_text('Database'))
action.perform()
action.move_to_element(driver.find_element_by_xpath("//span[text()='Items']"))
action.perform()
action.move_to_element(driver.find_element_by_link_text('Weapons'))
action.perform()
driver.find_element_by_link_text('Daggers').click()


num_of_items = int(driver.find_element_by_xpath('//*[@class="listview-note"]').text.split()[0])

filter_min_lvl = driver.find_element_by_name('minle')
filter_max_lvl = driver.find_element_by_name('maxle')
filter_max_lvl.send_keys('270')
filter_min_lvl.send_keys('213')
filter_max_lvl.send_keys(Keys.RETURN)

num_of_row = int(driver.find_element_by_xpath('//*[@class="listview-nav"]').text.split()[2])


# zoro = str(driver.page_source)

url_add = re.findall (r'(\w+)=(\d+)', driver.page_source) 

url_1 = [element for element in url_add if element[0]=='item']
url_set = set(url_1)
url_real = list(url_set)
df = pd.DataFrame({})

for i in range(10):
        wea = {}
        Stamina = None
        binds = None
        make = None
        Damage = None
        Speed = None
        DPS = None
        Intellect = None
        Agility = None
        Spirit = None
        Requrements = []
        Durability = None
        item_level = None
        green = []
        randon_enchantment = None
        chance_on_hit = None
        driver10 = webdriver.Chrome()
        driver10.get("https://wotlkdb.com/?item=" + url_real[i][1])
        item_discription = driver10.find_element_by_xpath("//tbody/tr[1]/td/table[1]/tbody/tr/td").text
        item_bonuses = driver10.find_element_by_xpath("(//TD)[4]/../../../..").text
        item_by_line = item_discription.split('\n')
        print(item_bonuses)
        Bonus = item_bonuses
        item_name = item_by_line[0]
        for str in item_by_line:
                if 'Binds' in str:
                        binds = str
                elif 'Hand' in str:
                        make = str
                elif 'Damage' and 'Speed' in str:
                        Damage = str.split(' ')[:2]
                        Speed = str.split(' ')[2:]
                elif 'damage per second' in str:
                        DPS = str
                elif 'Random enchantment' in str:
                        randon_enchantment = str
                        green.append(randon_enchantment)
                elif 'Stamina' in str:
                        Stamina = str.split(' ')[0]
                elif 'Intellect' in str:
                        Intellect = str.split(' ')[0]
                elif 'Agility' in str:
                        Agility= str.split(' ')[0]
                elif 'Spirit' in str:
                        Spirit= str.split(' ')[0]
                elif 'Chance on hit' in str:
                        chance_on_hit = str
                        green.append(chance_on_hit)
                elif 'Requires' in str:
                        Requrements.append(str)
                elif 'Durability' in str:
                        Durability = str
                elif 'Item Level' in str:
                        item_level = str
        wea = {
        'Item Name' : item_name,
        'Binds' : binds,
        'Make' : make,
        'Damage' : Damage,
        'Speed' : Speed,
        'DPS' : DPS,
        'Stamina' : Stamina,
        'Intellect' : Intellect,
        'Agility' : Agility,
        'Spirit' : Spirit,
        'Require' : Requrements,
        'Durability' : Durability,
        'Item Level' : item_level,
        'Bonus' : Bonus,
        'Additional' : green
        }
        df = df.append(wea, ignore_index=True)
df.to_csv('data_test.csv') 



    




















































































# driver.quit()