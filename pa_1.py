import requests
requests.get('http://www.baidu.com')

#打开有界面的网页
import selenium
from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get('http://www.baidu.com/')

#利用selenium和Chrome headless 驱动无界面网页
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://wwww.baidu.com')
driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup('<html></html>','lxml')

from pyquery  import PyQuery as pq
doc = pq('<html>hello</html>')
result = doc('html').text()
print(result)

#连接mysql
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='shuqi2555746',port=3306, db='mysql')
cursor =conn.cursor()
cursor.execute('select * from db')
print(cursor.fetchone())

import pymongo
client = pymongo.MongoClient('localhost')
db = client['newdb']

import redis
r = redis.Redis('localhost',6379)
r.set('name', 'bob')
print(r.get('name'))


