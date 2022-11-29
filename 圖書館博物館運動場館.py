import pandas as pd

df = pd.read_csv(
    'D:/D/TFT/全國運動場館資訊.csv', encoding='Big5')

df = df['縣市鄉鎮市區'].value_counts()

df.to_csv('D:/D/TFT/全國運動場館資訊數目.csv')
