# -*- coding: utf-8 -*-
import urllib2
import urllib

url = "http://127.0.0.1/php/test/mmms.php?st=1"

#--------------------- method 1 [GET]-------------------------
# response = urllib2.urlopen("hhttp://127.0.0.1/php/test/mmms.php?a=1&b=2&c=3")
# html = response.read()
# print html


#--------------------- method 2 [GET]-------------------------
# req = urllib2.Request("http://127.0.0.1/php/test/mmms.php?a=1&b=2&c=3")
# response = urllib2.urlopen(req)
# the_page = response.read()
# print the_page


#---------------------- method 3 [POST]-------------------------
# values = {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'x': 4,
# 	'y': 5,
# 	'z': 7,
# }
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# print response.read()

#----------------------- method 3_1 [GET]------------------------
# values = {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'x': 4,
# 	'y': 5,
# 	'z': 7,
# }
# url_get_param = urllib.urlencode(values)
# span = '&' if url.find('?') >= 0 else '?'
# new_url = url + span + url_get_param;
# req = urllib2.Request(new_url)
# response = urllib2.urlopen(req)
# print response.read()

#----------------------- method 4 [POST] --------------------------
# set headers
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {
# 	'x' : 10,
# 	'y' : 13,
# 	'z' : 55
# }
# headers = {
# 	'User-Agent' : user_agent,
# 	'x' : 'sfmafsf', # 随机数据
# 	'msd' : 'something special thin 

# data = urllib.urlencode(values)
# req = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(req)
# print response.read()

#----------------------- mothod 5 [urllib2.URLError]----------------------------
# req = urllib2.Request("http://www.baibai.com")
# try:
# 	urllib2.urlopen(req)
# except urllib2.URLError, e:
# 	print e.reason

#----------------------- mothod 5 [urllib2.URLError]----------------------------
# req = urllib2.Request("http://bbs.csdn.net/callmewhy")
# try:
# 	urllib2.urlopen(req)
# except urllib2.URLError, e:
# 	print e.code
# 	print e.reason

#------------------------ method 6 [urllib2.HTTPError, urllib2.URLError]----------
# req = urllib2.Request('http://bbs.csdn.net/callmewhy')
# try:
# 	response = urllib2.urlopen(req)
# except urllib2.HTTPError, e: # urllib2.HTTPError 要在 urllib2.URLError 之前 前者是后者的子类
# 	print 'The server couldn\'t fulfill the request.'
# 	print 'Error code: ', e.code
# except urllib2.URLError, e:
# 	print 'We failed to reach a server. '
# 	print 'Reason: ', e.reason
# else :
# 	print 'No exception was raised.'

#------------------------- method 7 [urllib2.URLError]-----------------------------------------
# req = urllib2.Request('http://bbs.csdn.net/callmewhy')
# try:
# 	response = urllib2.urlopen(req)
# except urllib2.URLError, e:
# 	if hasattr(e, 'code'):
# 		print 'The server couldn\'t fulfill the request.'
# 		print 'Error code: ', e.code
# 	elif hasattr(e, 'reason'):
# 		print 'We failed to reach a server.'
# 		print 'Reason: ', e.reason
# else:
# 	print 'No exception was raised.'

#------------------------- mothod 8 [geturl] ------------------------------------------
# old_url = 'http://rrurl.cn/b1UZuP'
# req = urllib2.Request(old_url)
# response = urllib2.urlopen(req);
# print 'Old url :' + old_url
# print 'Real url :' + response.geturl()

#------------------------- method 9 [info] --------------------------------------------
# old_url_baidu = 'http://www.baidu.com/'
# req = urllib2.Request(old_url_baidu)
# response = urllib2.urlopen(req)  
# print 'Info():'
# print response.info()


#-------------------------- method 10 [Auth] ----------------
auth_url = "http://127.0.0.1/php/test/msm.php"
values = {
	'a': 1,
	'b': 2,
	'c': 3,
	'x': 4,
	'y': 5,
	'z': 7,
	'user':'user',
	'passwd' :'passwd',
}
data = urllib.urlencode(values)
req = urllib2.Request(auth_url, data)
try:
	response = urllib2.urlopen(req)
except urllib2.HTTPError , e:
	print e.code, e.reason
except urllib2.URLError, e:
	print e.reason
else :
	print response.info()
	print response.read()

#--------------------------- method 11 [urllib2.Opener  urllib2.Handler ]---------------
# password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# top_level_url = "http://127.0.0.1/php/test/msm.php"

# password_mgr.add_password(None, top_level_url, 'user', 'passwd')

# handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# opener = urllib2.build_opener(handler)

# a_url = 'http://www.baidu.com/'

# opener.open(a_url)

# urllib2.install_opener(opener)
































































