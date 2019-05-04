import os
# os是跟系统相关的
# system 是跟python相关的

"""
1 个人用户环境变量 vi ~/.bash_profile 或者 vi ~/.bashrc
设置代理变量
.bashrc
# 代理变量
proxyhost="112.91.218.21"
proxyport="9000"
export proxyhost
export proxyport

立刻应用
source ~/.bashrc
"""

host = os.environ.get("proxyhost")
port = os.environ.get("proxyport")
print("http://{}:{}".format(host, port))

proxies = os.environ.get("http_proxy")
print(proxies)
