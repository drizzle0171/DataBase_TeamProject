from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import csv

browser = webdriver.Chrome('C:/chromedriver.exe')

browser.get('https://map.kakao.com/')
browser.implicitly_wait(30)

search = browser.find_element_by_css_selector('.query.tf_keyword')
search.send_keys('인천 서구 식당')
search.send_keys(Keys.ENTER)
time.sleep(2)


close = browser.find_element_by_css_selector('.view_coach')
close.click()
search_more = browser.find_element_by_css_selector('.option1 > a')
search_more.click()
time.sleep(3)

f = open(r'C:\Users\yongs\GDSC\DataBase_TeamProject\인천광역시 서구 식당 data_test.csv', 'w', encoding='CP949', newline = '')
csvWriter = csv.writer(f)

for whole_page_num in range(1, 2):
    for page_num in range(1, 6):     
        try: 
            next_page = browser.find_element_by_css_selector(f"#info\.search\.page\.no{page_num}")
            next_page.click()
            time.sleep(3)

            informations = browser.find_elements_by_css_selector('.PlaceItem.clickArea')

            for information in informations:
                name = information.find_element_by_css_selector("a.link_name").text
                address = information.find_element_by_css_selector("div.addr > p:nth-child(1)").text
                print(name, address)
                csvWriter.writerow([name, address])
        except:
            break
    else:
        next_btn = browser.find_element_by_css_selector("#info\.search\.page\.next")
        next_btn.click()
        
f.close()