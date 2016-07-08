# encoding: utf-8
import requests
import sys

from bs4 import BeautifulSoup



query = sys.argv[1]

url = 'https://number.whoscall.com/zh-TW/tw/'+query


WebSession = requests.Session()

WebSend = WebSession.post(url)
SourceCode = BeautifulSoup(WebSend.content , "html.parser")


NumberInfo = (SourceCode.find_all('h1',{'class':'number-info__name'}))

SpamNumber = (SourceCode.find_all('p',{'class':'number-info__category--spam'}))

NumberCategory = (SourceCode.find_all('p',{'class':'number-info__category'}))


NumberInfo = str(NumberInfo).split("\\n              ")[1].split("\\n")[0]
DecodeNumberInfo = NumberInfo.decode('unicode_escape')


print DecodeNumberInfo

if len(SpamNumber) == True:
	SpamNumber = str(SpamNumber).split("\\n              ")[1].split("\\n")[0]
	DecodeSpamNumber = SpamNumber.decode('unicode_escape')
	print '🚫',
	print ' '+DecodeSpamNumber
else:
	NumberCategory = str(NumberCategory).split("\\n              ")[1].split("\\n")[0]
	DecodeNumberCategory = NumberCategory.decode('unicode_escape')
	print DecodeNumberCategory




