import pandas as pd

df = pd.read_csv(
    'C:/Users/a1999/Desktop/資料/D槽\TFT/經緯度_all.csv', encoding='Big5')

df = df.drop(['地址'], axis=1)

print(df.head())
