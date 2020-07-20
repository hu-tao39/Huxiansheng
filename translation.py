import urllib.request
import urllib.parse
import json
import time

while True:
    content=input("请输入需要翻译的内容(输入“q！”退出程序：")
    if content=='q!':
        braek
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'

    data={}
    data['i']=content
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='15952289544754'
    data['sign']='9b7304f894b8cccc0eab325c878608f1'
    data['ts']='1595228954475'
    data['bv']='4b9de992aa3d23c2999121d735e53f9c'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_CLICKBUTTION'
    data=urllib.parse.urlencode(data).encode('utf-8')

    req=urllib.request.Request(url,data,head)
    response=urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')

    target=json.loads(html)
    target=target['translateResult'][0][0]['tgt']
    print(target)
    time.sleep(5)

