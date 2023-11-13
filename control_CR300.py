import requests
import json
import pandas as pd
import time
import random

from core import *

# 长客、唐客
changchun_cf300bf = [f'CR300BF-{tid}' for tid in range(5001, 5043)]
tangshan_cf300bf = [f'CR300BF-{tid}' for tid in range(3001, 3025)]

# 四方庞巴迪、中车四方、南京铺镇
sifang_pbd_cr300af = [f'CR300AF-{tid}' for tid in range(1001, 1015)]
sifang_qd_cr300af = [f'CR300AF-{tid}' for tid in range(2001, 2047)]
nanjing_cr300af = [f'CR300AF-{tid}' for tid in range(6001, 6005)]

cr300s = changchun_cf300bf + tangshan_cf300bf + sifang_pbd_cr300af +sifang_qd_cr300af+nanjing_cr300af
sumdf = []

for i in cr300s:
    time.sleep(3)
    
    print(f'{i}', end = '\r')
    
    # 从车列车编号枚举，交路信息逐车查询始发终到。
    tempdf = getTrainInfo(i)
    for j in range(len(tempdf)):
        try:
            
            train_no = tempdf[j]['train_no']
            traindateinfo = tempdf[j]['date'][0:4] + tempdf[j]['date'][5:7]+ tempdf[j]['date'][8:10]
            
            time.sleep(3)
            print(f'{i} {train_no} {traindateinfo}', end = '\r')

            tempRouteInfo = getTrainRoute(train_no, traindateinfo)
            tempdf[j]['from_station'] = tempRouteInfo['from_station']
            tempdf[j]['to_station'] = tempRouteInfo['to_station']
            tempdf[j]['total_num'] = tempRouteInfo['total_num']
            tempdf[j]['train_dbm'] = tempRouteInfo['train_no']
        except Exception as errinfo:
            print(f'error {errinfo} on {i}, {train_no}', end = '\r')    
    sumdf += tempdf
    
    

sumdf = pd.DataFrame(sumdf)
sumdf.to_excel('114514.xlsx')