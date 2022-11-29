import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import pandas as pd

options = Options()
options.add_argument("--disable-notifications")
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get('https://ap.ece.moe.edu.tw/webecems/pubSearch.aspx')

elem = chrome.find_element_by_id("btnSearch")

try:
    elem.click().submit()
except:
    pass
time.sleep(3)


name = []
county = []
town = []
num = []

for j in range(680):
    soup = BeautifulSoup(chrome.page_source, 'html.parser')

    divs = soup.find_all('div', {'class': 'kdCard-txt'})

    i = 0

    for d in divs:
        n = d.find('span', id='GridView1_lblSchName_'+str(i)).get_text()
        n = re.sub(r"</?(.+?)>", "", n)
        name.append(n)
        c = d.find('span', id='GridView1_lblCity_'+str(i)).get_text()
        c = re.sub(r"</?(.+?)>", "", c)
        county.append(c)
        t = d.find('span', id='GridView1_lblArea_'+str(i)).get_text()
        t = re.sub(r"</?(.+?)>", "", t)
        town.append(t)
        N = d.find('span', id='GridView1_lblGenStd_'+str(i)).get_text()
        N = re.sub(r"</?(.+?)>", "", N)
        num.append(N)

        i += 1
    if j != 679:
        next_page = chrome.find_element_by_id("PageControl1_lbNextPage")
        next_page.click()
        time.sleep(2)
    else:
        chrome.quit()


dict = {
    "名稱": name,
    "縣市": county,
    "鄉鎮": town,
    "招收人數": num
}

kindergarten_data = pd.DataFrame(dict)
kindergarten_data.to_csv(
    'C:/Users/a1999/Desktop/kindergarten_data.csv', encoding='utf_8_sig')

print('complete')
