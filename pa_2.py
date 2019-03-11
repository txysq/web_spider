from urllib  import request, parse
import urllib.request
#headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36' ,
          #'host':'httpbin.org'}
#url = 'http://www.httpbin.org/post'
#dict = {'name':'Germey'}
#data = bytes(parse.urlencode(dict), encoding='utf8')
#req = request.Request(url = url, data = data, headers=headers,method = 'POST')
#response = request.urlopen(req)
#print(response.read().decode('utf-8'))

import http.cookiejar, urllib.request #申明库
#cookie = http.cookiejar.CookieJar()    #申明cookie
#handler = urllib.request.HTTPCookieProcessor(cookie)  #创建cookie处理器
#opener = urllib.request.build_opener(handler) #建立打开
#response = opener.open('http://www.baidu.com')
#for item in cookie:
 #   print(item.name+'='+item.value)

filename = 'cookie.txt'
#cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt',ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))


from urllib import request, error
try:
    response = request.urlopen('http://www.baidu.com')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers)
except error.URLError s e:
    print(e.reason)
else:
    print('success')
