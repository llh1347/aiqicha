import json
import re
import requests
import time

time0 = time.time()

def push(msg):
    # 自用推送
    corpid = ''
    corpsecret = ''
    agentid = ''
    touser = '@all'

    value = json.dumps({
        'corpid': corpid,
        'corpsecret': corpsecret
    })
    res = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken', data=value)
    access_token = res.json()['access_token']
    # print(access_token)
    url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
    data = json.dumps({
        "touser": "@all",
        "msgtype": "text",
        "agentid": agentid,
        "text": {
            "content": msg  # 要推送的内容
        }})
    requests.post(url, data=data)


time0 = int(time0 * 1000)
url = f"http://service.100bt.com/creditmall/mall/page.jsonp?callback=jQuery17208031961396984637_1636644307871&pageIndex=9&pageSize=1&orderBy=1&_={time0}"

payload = {'pageIndex': '9',
           'pageSize': '1',
           'orderBy': '1'}
files = [

]
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'service.100bt.com',
    'Referer': 'http://www.100bt.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)
# print(response.text)#json报错
if response.status_code == 200:
    response = json.loads(re.findall("{.*}", response.text)[0])
    # print(response)
    if int(response["jsonResult"]["code"]) == 0:  # jsonResult.data.dataList[0].stockValue
        if response["jsonResult"]["data"]["dataList"][0]["stockValue"] > 0:
            print("奥拉星柔软抱枕有货了，快去兑换")
            push("奥拉星柔软抱枕有货了，快去兑换")
        else:
            print("奥拉星柔软抱枕无货")
    else:
        print("错误")

else:
    print('前方道路拥挤，请稍后再试~')
