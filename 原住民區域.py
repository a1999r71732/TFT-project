import pandas as pd

list = ['新北市烏來區', '桃園市復興區', '新竹縣尖石鄉', '新竹縣五峰鄉', '苗栗縣泰安鄉', '臺中市和平區', '南投縣信義鄉', '南投縣仁愛鄉', '嘉義縣阿里山鄉', '高雄市桃源區', '高雄市那瑪夏區', '高雄市茂林區', '屏東縣三地門鄉', '屏東縣瑪家鄉', '屏東縣霧臺鄉',
        '屏東縣牡丹鄉', '屏東縣來義鄉', '屏東縣泰武鄉', '屏東縣春日鄉', '屏東縣獅子鄉', '臺東縣達仁鄉', '臺東縣金峰鄉', '臺東縣延平鄉', '臺東縣海端鄉', '臺東縣蘭嶼鄉', '花蓮縣卓溪鄉', '花蓮縣秀林鄉', '花蓮縣萬榮鄉', '宜蘭縣大同鄉', '宜蘭縣南澳鄉']

df = pd.read_csv(
    'C:/Users/a1999/Desktop/資料/D槽\TFT/經緯度_all.csv', encoding='Big5')

indi = []
county = df['縣市鄉鎮市區'].values.tolist()
for i in range(len(df)):
    if county[i] in list:
        indi.append(1)
    else:
        indi.append(0)

df['原住民區'] = indi

df.to_csv('D:/D/TFT/原住民區.csv')
