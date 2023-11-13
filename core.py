import requests
import json
import pandas as pd
import time
import random

def randomWaitPause():
    time.sleep(random.randint(3,5))

# 爬取12306官方信息。函数缺陷：若日期不正确，可能会没有返回
def getTrainRoute(TrainKeyword = 'CR400BF-5033', traindateinfo='20231113'):
    url = f'https://search.12306.cn/search/v1/train/search?keyword={TrainKeyword}&date={traindateinfo}'
    resp = requests.get(url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})
    
    RouteInfo = json.loads(resp.text)
    # 多车返回第一个。如D376，可检索到D3760；D3761，目前只有D376是需要的
    return RouteInfo['data'][0]

    


# 爬取列车交路信息。可使用车体编号，如CR400BF-5033进行检索，也可使用车次如G1进行检索。
# 仅支持C、D、G字头的和谐号、复兴号列车。不支持Z字头的CR200J如Z5016，但支持C、D字头的
def getTrainInfo(TrainKeyword = 'CR400BF-5033'):
    url = f'https://api.rail.re/emu/{TrainKeyword}'
    resp = requests.get(url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})
    
    TrainInfo = json.loads(resp.text)
    return TrainInfo