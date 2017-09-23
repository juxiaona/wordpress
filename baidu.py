from selenium import webdriver
import unittest
import time
from base.base import Base

class BaiDu(unittest.TestCase):

	def setUp(self):
		self.dr=Base('chrome')
		self.dr.max_window()
		self.dr.open("http://www.baidu.com")

	def test_search1(self):
		'''self.dr.element_click('link_text', '登录')
		time.sleep(2)
		self.dr.change_element_attribute('class', 'pass-reglink','target','test')
		time.sleep(1)
		self.dr.element_click('link_text', '立即注册')
		time.sleep(2)

		self.dr.element_sendkeys('id', 'TANGRAM__PSP_3__userName', 'juxiaona')
		time.sleep(100)
		'''
		self.dr.add_cookies('BAIDUID', '8FAA0FC9CBF4AA62471A6D058540F731:FG=1')
		self.dr.add_cookies('BDUSS', 'JnM1p5aXg3SVZGckVTTEhxVVVKWEc4OEN5QjBKNXNmZ2pxRUQ5UjFGeEJtTkZaSVFBQUFBJCQAAAAAAAAAAAEAAABICuNWAAAAAA\
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEELqllBC6pZSG')
		self.dr.refresh()

	def tearDown(self):
		self.dr.quit()


if __name__ == '__main__':
	unittest.main()