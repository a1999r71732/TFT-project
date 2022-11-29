import pandas as pd

df = pd.read_csv('D:/D/TFT/學校到公所的行車距離未篩選.csv',
                 encoding='utf_8')

dis_list = []
dis = df['行車距離'].values.tolist()
for d in range(len(dis)):
    dis_value = dis[d]
    if dis_value != 'unknown':
        dis_value = float(dis_value[:-2])
        dis_list.append(dis_value)
    else:
        dis_list.append(100000)

df['driving_distance'] = dis_list

df = df.groupby(['Address'], dropna=False).driving_distance.min()

df.to_csv('D:/D/TFT/學校到公所最短行車距離.csv')
