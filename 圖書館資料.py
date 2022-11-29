import json
import pandas as pd

file = open('D:/D/TFT/公共圖書館基本資料.txt', 'r')
js = file.read()
dic = json.loads(js)

name = []
address = []
county = []
district = []
lng = []
lat = []

for i in range(len(dic)):
    name.append(dic[i]['圖書館名稱'])
    address.append(dic[i]['地址'])
    county.append(dic[i]['所屬縣市'])
    district.append(dic[i]['行政區'])
    lng.append(dic[i]['經度'])
    lat.append(dic[i]['緯度'])

dict = {
    '名稱': name,
    '地址': address,
    '縣市': county,
    '鄉鎮市區': district,
    '經度': lng,
    '緯度': lat
}

df = pd.DataFrame(dict)
df.to_csv('D:/D/TFT/公共圖書館基本資料.csv')

file.close()


# 圖書館名稱、地址、所屬縣市、行政區、經度、緯度
