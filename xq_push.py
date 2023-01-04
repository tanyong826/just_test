import requests, json, re
from bs4 import BeautifulSoup

# 企业微信推送参数
corpid = ''
agentid = ''
corpsecret = ''
touser = ''
# 推送加 token
plustoken = ''

#https://www.xiequ.cn/redirect.aspx?act=Product.aspx 获取cookie 只写了买流量包的推送 按次数计费的没有写
cookie ='这里填cookie'

def Push(contents):
    # 微信推送
    if all([corpid, agentid, corpsecret, touser]):
        token = \
        requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}').json()[
            'access_token']
        json = {"touser": touser, "msgtype": "text", "agentid": agentid, "text": {"content": "携趣流量剩余使用推送\n" + contents}}
        resp = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}", json=json)
        print('微信推送成功' if resp.json()['errmsg'] == 'ok' else '微信推送失败')

    if plustoken:
        headers = {'Content-Type': 'application/json'}
        json = {"token": plustoken, 'title': '携趣流量剩余使用推送', 'content': contents.replace('\n', '<br>'), "template": "json"}
        resp = requests.post(f'http://www.pushplus.plus/send', json=json, headers=headers).json()
        print('push+推送成功' if resp['code'] == 200 else 'push+推送失败')

url = 'https://www.xiequ.cn/Product.aspx'
headers = {
    'cookie': f'{cookie}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}
html = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')
a = soup.find_all('div',style="float:left;width:130px;font-size:13px;border-right:1px solid #A0A0A0;")
llzl = str(a[-2]).replace('<div style="float:left;width:130px;font-size:13px;border-right:1px solid #A0A0A0;">','').replace('</div>','')
llsy = str(a[-1]).replace('<div id="M325200" style="float:left;width:130px;font-size:13px;border-right:1px solid #A0A0A0;">','').replace('</div>','')
message =f'流量计费套餐: 套餐总量 {llzl} 已使用：{llsy}'
print(message)
Push(contents=message)
