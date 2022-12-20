import requests, os
from bs4 import BeautifulSoup

# 配置cookie 抓取https://www.52pojie.cn/forum.php域名cookie整段 支持多账号 一个引号里面一个cookie 自己根据实际情况增删
cookie = [
    '',
    ''
]

for i in range(len(cookie)):
    print(f'开始第{i+1}个帐号签到')
    headers = {
        "Cookie": f'{cookie[i]}',
        "ContentType": "text/html;charset=gbk",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    requests.session().put(
        "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2", headers=headers
    )
    fa = requests.session().put(
        "https://www.52pojie.cn/home.php?mod=task&do=draw&id=2", headers=headers
    )
    fb = BeautifulSoup(fa.text, "html.parser")
    fc = fb.find("div", id="messagetext").find("p").text
    if "您需要先登录才能继续本操作" in fc:
        print("Cookie 失效")
    elif "恭喜" in fc:
        print("签到成功")
    elif "不是进行中的任务" in fc:
        print("今日已签到")
    else:
        print("签到失败")
