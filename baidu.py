from selenium import webdriver
from baidu_page import BaiduPage
import unittest

class BaiDu(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("http://www.baidu.com")

	def test_search1(self):
		bd=BaiduPage(self.driver)
		bd.input_text('python')
		bd.button_click()

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()