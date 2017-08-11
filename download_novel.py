#-*-coding:utf-8-*-
#author:zlw
import re
import urllib
import urllib2

url="http://:www.xxbiquge.com/0_142/1006272.html" #第一章 
url1="http://www.xxbiquge.com/0_142/%s" 

def gethtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return  html

def get_name_content(html):
	re1=re.compile('<title>.+?</title>')
	re2=re.compile('<div id="content">.+?</div>')
	re3=re.compile('<a href="/0_142/\d+?.html">下一章</a>')
	s1=re1.findall(html)
	s2=re2.findall(html)
	s3=re3.findall(html)
	#去掉多余的内容
	if len(s1)>0 and len(s2)>0 and len(s3)>0:
		name=s1[0].replace('<title>','')
		name=name.replace('-大主宰 - 新笔趣阁</title>','')
		content=s2[0].replace('<div id="content">','')
		content=content.replace('<br /><br />','')
		content=content.replace('&nbsp;','')
		content=content.replace('</div>','')
		content=content.replace('readx();','')
		href=s3[0].replace('<a href="/0_142/','')
		href=href.replace('">下一章</a>','')
	else:
		name=''
		content=''
		href=''
	return name,content,href

def write_novel(href,file1):
	file1.writelines('\n\r')
	while href <> '':
		html = gethtml(url1 % href)
		name,content,href = get_name_content(html)
		file1.writelines(name)
		file1.writelines('\n\t')
		file1.writelines(content)
		file1.writelines('\n\t')
		file1.writelines(href)
		file1.writelines('\n\n\n')

file1=file('dzz.txt','w+')
[write_novel('1006272.html',file1)]
file1.close()
