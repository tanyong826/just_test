import requests,json,time

#etc助手小程序-萌兔送喜
#填入https://gw.etczs.net/api/activity/collect/card/lottery/draw请求头X-APP-TOKEN 支持多账号 格式
#X_APP_TOKEN = ['token1','token2']
X_APP_TOKEN = ['3ec8c86d38db6ec529a00d2ab8659eb848ad8610']

for i in range(len(X_APP_TOKEN)):
    print(f'********第{i+1}个帐号********')
    url = 'https://gw.etczs.net/api/activity/collect/card/lottery/draw'
    url2 = 'https://gw.etczs.net/api/activity/collect/card/part/homePage'
    headers = {
        'Host': 'gw.etczs.net',
        'Connection': 'keep-alive',
        'X-APP-ID': '1',
        'content-type': 'application/json',
        'X-APP-VER': '6.4.230105',
        'X-APP-TOKEN': f'{X_APP_TOKEN[i]}',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.32(0x1800202c) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wxb17f5d5d01db8949/1163/page-frame.html'
    }
    data = '{"activityCode":"collect_card"}'
    for j in range(5):
        print(f'开始第{j+1}次召唤')
        html = requests.post(url=url, headers=headers, data=data)
        result = html.json()['msg']
        print(result)
        time.sleep(1)
    html2 = requests.get(url=url2, headers=headers)
    result2=html2.json()['data']['collectCardCountDtoList']
    # print(result2)
    print('集卡情况：')
    for k in range(len(result2)):
        print(result2[k]['prizeName']+':'+result2[k]['cardNum'])
