import requests

# 使用get（）函数访问百度首页，函数返回对象r
r = requests.get('http://www.baidu.com')
print(r.text)
