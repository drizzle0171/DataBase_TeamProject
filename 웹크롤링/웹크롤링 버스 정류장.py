from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import csv

region = '부산 북구'
browser = webdriver.Chrome('C:/chromedriver.exe')

browser.get('https://map.kakao.com/')
browser.implicitly_wait(30)

search = browser.find_element_by_css_selector('.query.tf_keyword')
search.send_keys(f'{region} 버스')
search.send_keys(Keys.ENTER)
time.sleep(2)


close = browser.find_element_by_css_selector('.view_coach')
close.click()
search_more = browser.find_element_by_css_selector('#info\.main\.options > li.option4.option4-ACTIVE > a')
search_more.click()
#browser.find_element_by_css_selector('#info\.searchHeader\.message > div.BusMessageView > div:nth-child(2) > a').click()
time.sleep(3)

f = open(r'C:\Users\yongs\GDSC\DataBase_TeamProject\서울 관악구 요양원.csv', 'w', encoding='CP949', newline = '')
csvWriter = csv.writer(f)



for whole_page_num in range(1, 50):
    for page_num in range(1, 6):     

            next_page = browser.find_element_by_css_selector(f"#info\.search\.page\.no{page_num}")
            next_page.click()
            time.sleep(3)
            names = browser.find_elements_by_css_selector('div.para')

            for name in names:
                bus = name.find_element_by_css_selector('a.name').text
                print(bus)



    else:
        next_btn = browser.find_element_by_css_selector("#info\.search\.page\.next")
        next_btn.click()
        
f.close()
browser.close()