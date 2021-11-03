# 데이터베이스 웹크롤링

# 필요: 가게 이름, 분류
# 동적....페이지..........
# 셀레니움

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

browser = webdriver.Chrome('C:/chromedriver.exe')

# 카카오맵 열기
browser.get('https://map.kakao.com/')
browser.implicitly_wait(30)

search = browser.find_element_by_css_selector('.query.tf_keyword')
search.send_keys('인천 서구 식당')
search.send_keys(Keys.ENTER)
time.sleep(2)


# 안되는 부분 =====================================================================
# search_more = browser.find_element_by_xpath('//*[@id="info.search.place.more"]')
# search_more.click()
# time.sleep(3)
#=================================================================================

# 장소 더보기 후
# 페이지 넘기기
# 근데 url에 변화가 없는데 어떡하지?
# 일일이 버튼을 클릭해야 하나...?

informations = browser.find_elements_by_css_selector('.PlaceItem.clickArea')

for information in informations:
    name = information.find_element_by_css_selector("a.link_name").text
    address = information.find_element_by_css_selector("div.addr > p:nth-child(1)").text
    print(name, address)