import requests, json,re

#https://ikuuu.dev/auth/register?code=TCM6 这个是注册链接 一个免费的比较稳定的机场可以 
#https://ikuuu.dev/user登录后cookie

cookie ='这里配置登录有的cookie'

url_info = 'https://ikuuu.dev/user/profile'
url = 'https://ikuuu.dev/user/checkin'
headers = {
    'cookie': f'{cookie}',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}
html_info = requests.get(url=url_info, headers=headers).text
html = requests.post(url=url, headers=headers)
result = json.loads(html.text)['msg']
info = "".join(re.findall('<div class="d-sm-none d-lg-inline-block">(.*?)</div>', html_info, re.S))
print(info+'\n'+result)
