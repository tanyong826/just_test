import requests, re,time,json,datetime
from bs4 import BeautifulSoup

# 签到+摇摇乐
# 配置帆软社区cookie 单引号里面填帆软网页的cookie就可以了
cookie = ''


# 企业微信推送参数
corpid = ''
agentid = ''
corpsecret = ''
touser = ''
# 推送加 token
plustoken = ''

def Push(contents):
    # 微信推送
    if all([corpid, agentid, corpsecret, touser]):
        token = \
        requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}').json()[
            'access_token']
        json = {"touser": touser, "msgtype": "text", "agentid": agentid, "text": {"content": "帆软签到\n" + contents}}
        resp = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}", json=json)
        print('微信推送成功' if resp.json()['errmsg'] == 'ok' else '微信推送失败')

    if plustoken:
        headers = {'Content-Type': 'application/json'}
        json = {"token": plustoken, 'title': '帆软签到', 'content': contents.replace('\n', '<br>'), "template": "json"}
        resp = requests.post(f'http://www.pushplus.plus/send', json=json, headers=headers).json()
        print('push+推送成功' if resp['code'] == 200 else 'push+推送失败')

date = time.strftime("%Y%m%d",time.localtime())

# 获取formhash
url = 'https://bbs.fanruan.com/plugin.php?id=k_misign:sign'
checksign_url ='https://bbs.fanruan.com/qiandao/'
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://bbs.fanruan.com/qiandao/',
    'cookie': f'{cookie}',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
response = requests.get(url=url, headers=headers).text
formhash = ''.join(re.findall('formhash=(.*?)">退出</a></li>', response, re.S))
# print(formhash)
# 签到
sign_url = f'https://bbs.fanruan.com/qiandao/?mod=sign&operation=qiandao&formhash={formhash}&from=insign&inajax=1&ajaxtarget=JD_sign'
sign_re = requests.get(url=sign_url, headers=headers).text
check_re = requests.get(url=checksign_url, headers=headers).text
user = str(re.findall('" c="1" class="author">(.*?)</a>', str(check_re), re.S)).replace('[','').replace(']','').replace('\'','')
sign_rank = str(re.findall('<input type="hidden" class="hidnum" id="qiandaobtnnum" value="(.*?)">', str(check_re), re.S)).replace('[','').replace(']','').replace('\'','')
lxdays = str(re.findall('<input type="hidden" class="hidnum" id="lxdays" value="(.*?)">', str(check_re), re.S)).replace('[','').replace(']','').replace('\'','')
lxtdays = str(re.findall('<input type="hidden" class="hidnum" id="lxtdays" value="(.*?)">', str(check_re), re.S)).replace('[','').replace(']','').replace('\'','')

# 摇摇乐
yyl_url = 'https://bbs.fanruan.com/plugin.php?id=yinxingfei_zzza:yinxingfei_zzza_post'
yyl_info_url = 'https://bbs.fanruan.com/plugin.php?id=yinxingfei_zzza:yinxingfei_zzza_hall'
yyl_data = dict(id='yinxingfei_zzza:yinxingfei_zzza_post', formhash=f'{formhash}')
yyl_re = requests.post(url=yyl_url, headers=headers, data=yyl_data).text
yyl_info = requests.post(url=yyl_info_url, headers=headers).text
result = str(re.findall(f'<td class="zzza_{date} zzza_signed_anime_day" title="(.*?)">', str(yyl_info), re.S)).replace('[','').replace(']','').replace('\'','')

massage= "签到信息 "+ date + '\n' + user +'\n'+'已签到 今天签到排名：' + sign_rank + ' 连续签到天数：' + lxdays + ' 总天数：'+lxtdays+'\n'+"摇摇乐信息 "+ '\n'+result
print(massage)

Push(contents=massage)

