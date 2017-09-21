from selenium import webdriver
from time import sleep
from base.base import Base
import unittest

class Test(unittest.TestCase):

	def setUp(self):

		self.dr=Base('chrome')
		self.dr.max_window()
		self.dr.open("https://guanjia.xxkuaipao.com/login")

	def test_case(self):

		self.dr.element_sendkeys('id', 'frc-name-1088', 'ppytest')
		self.dr.element_sendkeys('id', 'frc-pwd-1088', 'ppy123')
		self.dr.element_click('class', 'submit')
		sleep(2)
		self.dr.open('https://guanjia.xxkuaipao.com/user/list')
		self.dr.element_click('link_text', '添加会员')
		sleep(2)
		self.dr.set_date('class', 'react-datepicker__input', '2017-09-21')

		self.dr.element_sendkeys('class', 'wrap-image-upload', '../data/1.jpg')
		sleep(2)



	def tearDown(self):
		self.dr.quit()


if __name__ == '__main__':
	
	unittest.main()


  