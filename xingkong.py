import requests, json

#配置星空代理http://www.xkdaili.com/main/usercenter.aspx 的cookie 支持多账号 一行一个cookie填单引号里 根据实际需求删减 
cookie = [
    '',
    '',
    ''
]

for i in range(len(cookie)):
    print(f'开始第{i + 1}个帐号签到')
    url = 'http://www.xkdaili.com/tools/submit_ajax.ashx?action=user_receive_point'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '10',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': f'{cookie[i]}',
        'Host': 'www.xkdaili.com',
        'Origin': 'http://www.xkdaili.com',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.xkdaili.com/main/usercenter.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data={
        'type': 'login'
    }
    html = requests.post(url=url, headers=headers, data=data)
    result = json.loads(html.text)['msg']
    print(result)
