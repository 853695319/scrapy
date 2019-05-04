import requests
from bs4 import BeatifulSoup

def zhihu_login():
    # 实例化session对象，可以保存cookie
    sess = requests.session()

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # get方法获取需要的cookie
    html = sess.get('https://www.zhihu.com/signin'， headers=headers)

    # 防止跨站请求伪造,通过GET方法得到它，然后POST才能成功
    _xrsf = sess.cookies.get('_xrsf')
    print(_xrsf)

    # post方法登录

    # 输入验证码，现在验证码是点击登录后，再PUT方法生成的，不简单

