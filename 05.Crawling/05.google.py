import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome('./chromedriver.exe')
driver.get('http://www.google.com')

# time.sleep(3)
search_box = driver.find_element_by_name("q")
# seach_box = driver.find_element_by_css_selector('#input')
search_box.send_keys('ChromeDriver')
search_box.submit()


# time.sleep(3)

''' title_list = []
content_list = []
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
divs = soup.select('.g')
for div in divs:
    title = div.select_one(".LC20lb.DKV0Md").get_text()
    content = div.select_one(".aCOpRe").get_text()
    title_list.append(title)
    content_list.append(content)
df = pd.DataFrame({
    title : title_list, content : content_list
})
df.to_csv('google.csv',sep='|') '''
# driver.close()

title_list = []
content_list = []
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
divs = soup.select('.g')
for div in divs:
    title = div.select_one(".LC20lb.DKV0Md").get_text()
    content = div.select_one(".aCOpRe").get_text()
    title_list.append(title)
    content_list.append(content)
df = pd.DataFrame({
    title : title_list, content : content_list
})
df.to_csv('google.csv',sep='|')