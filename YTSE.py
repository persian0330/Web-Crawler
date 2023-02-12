'''
This code is used for simplify the precess of submitting form data on an certain website.
Implemented:
    Simulate the login process
    Send GET request to get web page information after login
    Send POST request to the web page to submit the prepared form data
'''


from urllib import request
from http.cookiejar import CookieJar
from urllib import parse

url = 'http://118.31.21.104:8092/YTSE/user/index'
url_login = 'http://118.31.21.104:8092/YTSE/user/login'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Referer': 'http://yantaisei.sdsei.org.cn:8092/YTSE/user/index'
}

#登录
#1.1创建cookiejar对象
cookiejar = CookieJar()
#1.2用cookiejar创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
#1.3使用上一步创建的handler创建一个opener
opener = request.build_opener(handler)
#1.4使用opener发送登录请求

login_data = parse.urlencode({
    'username': 'songyang',
    'password': '123'
})

req = request.Request(url_login,data=login_data.encode('utf-8'))
opener.open(req)
'''
#2访问个人界面
rq = request.Request(url,headers=headers)
resp = opener.open(rq)
print(resp.read().decode('utf-8'))
'''

select_data = parse.urlencode({
    'zhucedaima': '',
    'shebeizhongleidaima':'',
    'jianyanleibie':'',
    'shiyongdengjibianhao':'F01240',
    'quhuadaima':'',
    'shouliriqi':'',
    'chanpinbianhao':'',
    'shiyongdanwei':'',
    'page': '1',
    'rows': '10'
})
rq = request.Request('http://118.31.21.104:8092/YTSE/renwu/rwlist',headers=headers,data=select_data.encode('utf-8'))

resp = opener.open(rq)
print(resp.read().decode('utf-8'))








#点击我的任务url：http://118.31.21.104:8092/YTSE/renwu/skip/myrw_list?note=b788b25fa28211e79a1400163e050907&time=1584619841622&_=1584619581729
#get请求数据：
#note: b788b25fa28211e79a1400163e050907(疑似id)
#time: 1584619841622
#_: 1584619581729

#获取任务列表：http://118.31.21.104:8092/YTSE/renwu/rwlist
#post请求数据：
#page: 1
#rows: 10

#获取区域名称url：http://118.31.21.104:8092/YTSE/dicArea/getAreaListById?id=370600
#post请求数据：
#id: 370600

#查找请求url：http://118.31.21.104:8092/YTSE/renwu/rwlist
#post请求数据：
#zhucedaima: 21203706112013120005
#shebeizhongleidaima:
#jianyanleibie:
#shiyongdengjibianhao:
#quhuadaima:
#shouliriqi:
#chanpinbianhao:
#shiyongdanwei:
#page: 1
#rows: 10

#点击检验报告url：ttp://118.31.21.104:8092/YTSE/flow/skip/flow_list?note=aef8f12e71b211e78e8400163e050907&time=1584705269529&_=1584705053510
#get请求数据：
#note: aef8f12e71b211e78e8400163e050907
#time: 1584705269529
#_: 1584705053510

#查看报告清单url：http://118.31.21.104:8092/YTSE/flow/list
#post请求数据：
#表单数据form data：
#page：1
#rows：10

#编辑报告url：http://118.31.21.104:8092/YTSE/flow/getById?flowId=06f8f3a06a9d11eaa545ce06b36e1107&sbzl=2000&time=1584705494934&_=1584705053512
#get请求数据：
#flowId: 06f8f3a06a9d11eaa545ce06b36e1107
#sbzl: 2000
#time: 1584705494934
#_: 1584705053512

#检查modelbyid url：http://118.31.21.104:8092/YTSE/report/checkModelById
#post请求数据：
#modelId: 108
#batchIds: 06f8f3a06a9d11eaa545ce06b36e1107

#获取详细报告信息：ttp://118.31.21.104:8092/YTSE/2000/getReportById?annalid=05149b196a9d11eaa545ce06b36e1107&note=_1584705494934&time=1584705577329&_=1584705053513
#get请求数据：
#annalid: 05149b196a9d11eaa545ce06b36e1107
#note: _1584705494934
#time: 1584705577329
#_: 1584705053513