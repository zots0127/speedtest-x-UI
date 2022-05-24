from urllib import request
import json
import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
#%matplotlib inline
from datetime import datetime
import time
def gettime(created):
    h=int(datetime.strftime(datetime.strptime(created,"%Y-%m-%d %H:%M:%S"), "%H"))
    m=int(datetime.strftime(datetime.strptime(created,"%Y-%m-%d %H:%M:%S"), "%M"))*100/6000
    return str(h+m)
def scaletime(time):
    return time*60/100
while True:
    response = request.urlopen("https://vis.lab.bojun.wang/backend/results-api.php")
    html = response.read()
    #print(html)
    jsondata=json.loads(html)
    df = pd.DataFrame(jsondata['data'])
    df = df.drop(columns=['key'])
    new = df[df['_id'] > 1655]
    new = new.drop(columns=['_id'])
    new = new[new['uspeed'] > 0]
    new['hr'] = new.apply(lambda x: gettime(x.created), axis=1)
    new.to_csv("new.csv")
    df = df.drop(columns=['_id'])
    df.to_csv("raw.csv")
    df['hr'] = df.apply(lambda x: gettime(x.created), axis=1)
    us = df[df["addr"].str.contains('United States')]
    us.to_csv("us.csv")
    kr = df[df["addr"].str.contains('South Korea')]
    kr.to_csv("kr.csv")
    df = df[df['jitter'] < 400]
    df = df[df['ping'] < 300]
    df = df[df['uspeed'] < 500]
    df = df[df['dspeed'] < 500]

    cn = df[df["addr"].str.contains('China', case=False)]
    cn.to_csv("cn.csv")
    withoutupload = df[df['uspeed'] == 0]
    withoutupload.to_csv("noupload.csv")
    didupload = df[df['uspeed'] > 0]
    didupload = didupload[didupload['uspeed'] < 500]
    didupload = didupload[didupload['dspeed'] < 500]
    didupload.to_csv("didupload.csv")
    didupload = didupload[didupload['jitter'] > 0]
    clean = didupload[didupload['ping'] > 145]
    clean = clean[clean['ping'] < 300]
    clean = clean[clean['jitter'] < 200]

    clean.to_csv("normal.csv")
    combine =didupload.replace('China Telecom Shanghai','China Telecom')
    combine =combine.replace('China Telecom Beijing','China Telecom')
    combine =combine.replace('China Unicom Beijing','China Unicom')
    combine =combine.replace('China Unicom Liaoning','China Unicom')
    combine =combine.replace('China Unicom Shanghai','China Unicom')
    combine =combine.replace('China Unicom Shenzen','China Unicom')
    combine =combine.replace('China Unicom Guangdong','China Unicom')
    combine =combine.replace('China Mobile Guangdong','China Mobile')
    combine =combine.replace('Henan Mobile Communications Co.,Ltd','China Mobile')
    combine =combine.replace('China Mobile Shandong','China Mobile')
    combine =combine.replace('China Telecom Guangdong province Dongguan MAN net','China Telecom')
    combine =combine.replace('CHINATELECOM Guangdong province Jieyang 5G network','China Telecom')
    combine =combine.replace('CHINATELECOM Guangdong province Chaozhou 5G networ','China Telecom')
    combine =combine.replace('CHINATELECOM Guangdong province Shantou 5G network','China Telecom')
    combine =combine.replace('CHINATELECOM Guangdong province Shaoguan 5G networ','China Telecom')
    combine =combine.replace('China Telecom Guangdong province Guangzhou MAN net','China Telecom')
    combine =combine.replace('China Telecom Guangdong province Dongguan MAN netw','China Telecom')
    combine =combine.replace('CHINATELECOM Guangdong province Zhanjiang 5G netwo','China Telecom')
    combine =combine.replace('China Unicom Guangzhou','China Unicom')
    combine =combine.replace('China Telecom Guangdong province Foshan MAN networ','China Telecom')
    combine =combine.replace('China Telecom Guangdong province Yuexi MAN network','China Telecom')
    combine =combine.replace('China Mobile Hebei','China Mobile')
    combine =combine.replace('China Telecom TIANJIN','China Telecom')
    combine =combine.replace('China Telecom Guangdong province Yuedong MAN netwo','China Telecom')
    combine =combine.replace('China Telecom Guangdong','China Telecom')
    combine =combine.replace('CHINATELECOM Guangdong province Zhuhai 5G network','China Telecom')

    #combine['isp'].unique()
    combine.to_csv("clean.csv")
    cnclean = combine[combine["addr"].str.contains('China', case=False)]
    cnclean.to_csv("cnclean.csv")
    CT = combine[combine['isp'] == 'China Telecom']
    CM = combine[combine['isp'] == 'China Mobile']
    CU = combine[combine['isp'] == 'China Unicom']
    frames = [CT,CM,CU]
    CN = pd.concat(frames)
    CN.to_csv("CN.csv")
    CT.to_csv("CT.csv")
    CM.to_csv("CM.csv")
    CU.to_csv("CU.csv")
    #print("Refresh!")
    time.sleep(5)