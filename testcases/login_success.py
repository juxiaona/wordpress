import sys
sys.path.append("../")

from pages.login_page import LoginPage
import unittest
from time import sleep

class LoginSuccess(unittest.TestCase):
	
	def setUp(self):

		self.login_success=LoginPage()

	def test_login_success(self):

		username='admin'
		password='jxn461028'

		self.login_success.login(username,password)
		text=self.login_success.get_login_success_text()
		self.assertIn(username, text)

		url=self.login_success.get_login_success_url()
		self.assertIn('wp-admin', url)

	def tearDown(self):
		self.login_success.quit()



if __name__ == '__main__':
	unittest.main()