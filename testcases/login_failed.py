import sys
sys.path.append("../")
from pages.login_page import LoginPage
import unittest
from time import sleep

class LoginFailed(unittest.TestCase):

	@classmethod
	def setUpClass(self):

		self.login_failed=LoginPage()
	
	def test_login_no_username(self):

		username=''
		password='jxn461028'
		self.login_failed.login(username, password)
		error_msg=self.login_failed.get_login_error_text()
		self.assertEqual('错误：用户名一栏为空。', error_msg)
		sleep(2)

	def test_login_no_password(self):

		username='admin'
		password=''

		self.login_failed.login(username, password)
		error_msg=self.login_failed.get_login_error_text()
		self.assertEqual('错误：密码一栏为空。', error_msg)
		sleep(2)
	
	def test_login_error_password(self):

		#username='admin'
		#password='123456'
		self.login_failed.login('admin', '123456')
		error_msg=self.login_failed.get_login_error_text()
		self.assertEqual('错误：为用户名admin指定的密码不正确。 忘记密码？', error_msg)
		sleep(2)
	
	def test_login_error_username(self):

		username='test'
		password='jxn461028'
		self.login_failed.login(username, password)
		error_msg=self.login_failed.get_login_error_text()
		self.assertEqual('错误：无效用户名。 忘记密码？', error_msg)
		sleep(2)
	
	@classmethod
	def tearDownClass(self):

		self.login_failed.quit()

if __name__ == '__main__':

	unittest.main()
