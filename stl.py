import requests, json

# https://www.stlxz.com/登录后cookie
cookie = '这里填cookie'

url = 'https://www.stlxz.com/wp-admin/admin-ajax.php?action=checkin_details_modal'
headers = {
    'cookie': f'{cookie}',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'origin': 'https://www.stlxz.com',
    'referer': 'https://www.stlxz.com/wl/wzzjc/12021.html'
}
data = {
    'action': 'user_checkin'
}
html = requests.post(url=url, headers=headers,data=data)
result = json.loads(html.text)['msg']
print(result)
