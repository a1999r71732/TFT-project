import pandas as pd


df = pd.read_csv(
    'C:/Users/a1999/Desktop/資料/D槽\TFT/kindergarten_data.csv', encoding='Big5')

df = df.groupby(['縣市鄉鎮市區']).招收人數.sum()
print(df.head())

df.to_csv('D:/D/TFT/幼稚園招收人數總數(依鄉鎮市區).csv')
