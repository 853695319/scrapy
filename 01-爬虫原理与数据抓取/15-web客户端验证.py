import urllib.request


"""
目标：是那种以登陆就要求输入账号密码的IP，很少见
"""

# 下面的内容也可以写入到环境变量
username = "test"
password = "123456"
webserver = "192.168.1.104"
proxyserver = "192.168.1.104:8000"

# 1 构建一个密码管理对象， 可以用来保存和HTTP请求相关的授权账户信息
passwrod_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 2 添加账户信息，第一个 域 realm 如果没有指定就None, 后三个 站点IP， 账户和密码
passwrod_mgr.add_password(None, webserver, username, password)

# 3.1 基于HTTP基础验证类创建HTTPHandle
http_handle = urllib.request.HTTPBasicAuthHandler(passwrod_mgr)

# 3.2 基于代理基础验证类创建HTTPHandle, 授权代理处理器，不过一般用环境变量的方法，比较简单方便
proxy_handle = urllib.request.ProxyBasicAuthHandler(passwrod_mgr)

# 4 创建opener
opener = urllib.request.build_opener(http_handle)
# opener 可以有多个HTTPHandle
# def build_opener(*handlers) *handlers 不定长参数，可以有多个HTTPHandle
# opener = urllib.request.build_opener(http_handle, proxy_handle)


# 5 请求响应
request = urllib.request.Request("http://{}/".format(webserver))
response = opener.open(request)
print(response.read())