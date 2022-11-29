import pandas as pd
import googlemaps


df = pd.read_csv('D:/D/TFT/distance_2.csv',
                 encoding='Big5', index_col='Address')  # 讀檔

origin = df[['origin_lat', 'origin_lng']].values.tolist()
destination = df[['緯度', '經度']].values.tolist()

gmaps = googlemaps.Client(
    key='AIzaSyARhqJWIFH6jD4WkwUO0DB_1Us4Gd85K1s')  # 輸入金鑰
dis = []
dis_2 = []
time = []
count = 0
for i in range(len(df)):

    result = gmaps.distance_matrix(origins=(origin[i][0], origin[i][1]), destinations=(destination[i][0], destination[i][1]), mode='driving', avoid=None,
                                   language='zh-TW', departure_time=None, arrival_time=None, transit_mode=None,
                                   transit_routing_preference=None, traffic_model=None)
    if result['rows'][0]['elements'][0]['status'] != 'ZERO_RESULTS':
        d = result['rows'][0]['elements'][0]['distance']['text']
        dis.append(d)
        d = float(d[:-2])  # 去掉公里
        d = str(d*2)+" "+"公里"  # 加權，再把公里加回來
        dis_2.append(d)
        t = result['rows'][0]['elements'][0]['duration']['text']
        time.append(t)
    else:
        dis.append('unknown')
        dis_2.append('unknown')
        time.append('unknown')
    count += 1
    print(count)

df['行車距離(未加權)'] = dis
df['行車距離'] = dis_2
df['時間'] = time

df.to_csv('D:/D/TFT/學校到二級車站的距離.csv')
print('finish')
