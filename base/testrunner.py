import sys
sys.path.append("../")
import time
from base.HTMLTestRunner import HTMLTestRunner
from base.sendmail import SendMail
import unittest

class TestRunner():

	def __init__(self,cases,title,description):
		
		self.cases=cases
		self.title=title
		self.description=description



	def run(self):

		discover=unittest.defaultTestLoader.discover(self.cases,pattern="*.py")
		
		now=time.strftime('%Y-%m-%d_%H_%M_')
		filename="./report/"+now+"report.html"
		fp=open(filename,"wb")
		runner=HTMLTestRunner(stream=fp,title=self.title,description=self.description)

		runner.run(discover)

		fp.close()
		'''发送邮件'''
		mail=SendMail('smtp.163.com', 'ju_xiaona@163.com', 'jxn461028', 'juxiaona@xxkuaipao.com')
		mail.sendmail(filename)

		

