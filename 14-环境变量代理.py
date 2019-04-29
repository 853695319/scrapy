import urllib.request
import os


# http请求
request = urllib.request.Request("http://www.baidu.com/")

# 1 构建一个代理处理器，参数是字典，不能为空， 可以为空字典
# 注意，如果你明确知道该代理是HTTP协议还是HTTPS协议，那么速度可以更快
# 实际上，代理一般不直接记录在程序里，通常通过倒入模块，或者设置环境变量
# 用处是将需要授权的代理账户和密码记录在环境变量里，这样就不怕别人使用你的代理

# 获取环境变量
proxy = "{}:{}".format(
    os.environ.get("proxyhost"), os.environ.get("proxyport")
)
http_proxy_handle = urllib.request.ProxyHandler({
    "http": "http://" + proxy,
})

# ！！关键变化：不指定 proxies ，使用系统变量里设置的代理变量 <protocol>_proxy
# http_proxy=http://112.91.218.21:9000
# export http_proxy
null_proxy_handle = urllib.request.ProxyHandler()

# 代理开关
# 切换到False 使用环境变量，True 程序设置代理
proxy_swith = True
# 注意区分
if proxy_swith:
    opener = urllib.request.build_opener(http_proxy_handle)
else:
    opener = urllib.request.build_opener(null_proxy_handle)

# 2 tip:构建一个全局opener，之后所有请求都可以用urlopen()方式去发送，也附带handle的功能
urllib.request.install_opener(opener)

# 3 响应请求
response = urllib.request.urlopen(request)

print(response.read())
# 有时候使用代理平台返回的编码格式是gbk，表示是从win发来的，可以进行编码
# print(response.read().decode("gbk"))
print(response.getcode())
