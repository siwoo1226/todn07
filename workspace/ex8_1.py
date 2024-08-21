from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.naver.com")
driver.implicitly_wait(0.5)
query_text="호드리구 소속팀"
search_box=driver.find_element(by=By.CSS_SELECTOR,value="#query")
search_box.send_keys(query_text)
search_button=driver.find_element(by=By.ID,value="search-btn")
search_button.click()
temp_div=driver.find_element(by=By.CSS_SELECTOR,value="#main_pack > section.sc_new.cs_common_module.case_normal._au_people_content_wrap.color_14._cs_sports_people > div.cm_content_wrap._content > div.cm_content_area._cm_content_area_profile > div > div.detail_info._detail_info_wrap > dl > div:nth-child(3) > dd > span > a")
print("20219 성시우")
print(temp_div.text)
time.sleep(10)

