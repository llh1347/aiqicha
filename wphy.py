 #爱企查京东e卡库存监控，只写了tg推送，改一下第9，10行的内容即可
#不要问cron怎么写，自己看自己机器决定，再问就是* * * * * *
from requests import get, post
from random import choice
import os
import json
import requests
def get_ua(brower_name):
    url = 'https://raw.githubusercontent.com/limoruirui/misaka/master/user-agent.json'
    useragent = choice(get(url).json()[brower_name])
    return useragent
def tgpush(content):
    bot_token = token
    user_id = id
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'chat_id': str(user_id), 'text': content, 'disable_web_page_preview': 'true'}
    try:
        req = post(url, headers=headers, data=data)
    except:
        print('推送失败')
def pushplus_bot(title, content):
    try:
        print("\n")
        print("PUSHPLUS服务启动")
        url = 'http://www.pushplus.plus/send'
        data = {
            "token": pushplus,
            "title": title,
            "content": content
        }
        body = json.dumps(data).encode(encoding='utf-8')
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, data=body, headers=headers).json()
        if response['code'] == 200:
            print('推送成功！')
        else:
            print('推送失败！')
    except Exception as e:
        print(e)
# 企业微信 APP 推送
   
def randomstr(numb):
    str = ''
    for i in range(numb):
        str = str + choice('abcdefghijklmnopqrstuvwxyz0123456789')
    return str
def get_status():
    url = 'https://aiqicha.baidu.com/usercenter/getBenefitStatusAjax'
    headers = {
      'User-Agent': get_ua('Safari'),
      'Referer': f'https://aiqicha.baidu.com/m/usercenter/exchangeList?VNK={randomstr(8)}'
    }
    if get(url, headers=headers).json()['data']['AQ03010'] == 1:
        tgpush('网盘会员有货，速去偷撸～')
        pushplus_bot('网盘会员监控', '网盘会员有货，速去偷撸～')
    else:
        print('网盘会员无货')
if __name__ == '__main__':
    id = os.environ["id"]
    token = os.environ["token"]
    pushplus = os.environ["pushplus"]
    get_status()
