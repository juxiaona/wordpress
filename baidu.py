from selenium import webdriver
import unittest

class BaiDu(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("http://www.baidu.com")

	def test_search1(self):
		self.driver.find_element_by_id("kw").send_keys('python')
		self.driver.find_element_by_id('su').click()

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()