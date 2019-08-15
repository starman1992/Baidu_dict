#有道翻译
import urllib.request as r
import urllib.parse as p
import json
import time
import random
import _md5
import hashlib

def process(url,data):
    #使用urlencode方法转换标准格式
    data = p.urlencode(data).encode('utf-8')
    #先定义header则需要在()中加入',head',后定义不用
    req = r.Request(url,data)   
        #后定义header则需要用到add_header函数
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
                    (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    #传递Request对象和转换完格式的数据
    response = r.urlopen(req,data)
    #读取信息并解码(\uxxxx为unicode模式)
    html = response.read().decode('utf-8')
    #使用JSON
    target =json.loads(html)
    return target
    
def Baidu(onlyone=1,content=None):
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    ##head = {}
    ##head['User-Agent']= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
    ##                    (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

    data = {}
    data['from']= 'en'
    data['to']= 'zh'
    data['appid']= '20151113000005349'
    data['salt']= random.randint(32768, 65536).__str__()
    secretKey = 'osubCEzlGjzvw8qdQc41'

    while onlyone==1:
        data['query'] = input('请输入要翻译的内容(输入"q!"结束)：')
        if data['query'] == 'q!':
            break
                
        sign = data['appid']+data['query']+data['salt']+secretKey
        data['sign'] = hashlib.md5(sign.encode(encoding='gb2312')).hexdigest()
        
        target = process(url,data)
        print(target)
        #print("百度翻译结果：%s" % (target['trans_result'][0]['dst']))
        time.sleep(3)   #系统休息3秒钟
