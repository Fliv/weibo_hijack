import requests
import json

folder = "data/"

def get_session(sina):
    if not sina.get('ticket'):
        return None
    login_url = "https://passport.weibo.com/wbsso/login"
    params = {'ticket': sina['ticket'],
              'ssosavestate': '1540189142',
              'callback': 'sinaSSOController.doCrossDomainCallBack',
              'scriptId': 'ssoscript0',
              'client': 'ssologin.js(v1.4.19)',
              '_': '1508653141866'}
    session = requests.session()
    r = session.get(login_url, params=params)
    with open(folder + sina['uid'] + '.cookies', 'w+') as fp:
        # json.dump(r.cookies._cookies, fp)
        fp.write(str(r.headers))
        fp.write("\r\n\r\n")
        fp.write(r.content)
    return session


def save_ticket(msg):
    sina = json.loads(msg)
    if sina.get('uid'):
        with open(folder + sina['uid'] + '.ticket', 'w+') as fp:
            json.dump(sina, fp)
    return sina


def send_weibo(content, session, uid):
    url = 'https://weibo.com/aj/mblog/add?ajwvr=6&__rnd=1508653972449'
    data = {'location': 'v6_content_home', 'text': content, 'appkey': '', 'style_type': '1', 'pic_id': '', 'tid': '',
            'pdetail': '', 'rank': '0', 'rankid': '', 'module': 'stissue', 'pub_source': 'main_', 'pub_type': 'dialog',
            'isPri': '0', '_t': '0'}
    headers = {'Referer': 'https://weibo.com/u/{uid}/home?wvr=5'.format(uid=uid),
               'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    session.headers.update(headers)
    r = session.post(url, data=data, proxies={"https": "https://127.0.0.1:8080"}, verify=False)
    print r.content
    pass
