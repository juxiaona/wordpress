import sys
sys.path.append("../")
from base.base import Base

class LoginPage():

	def __init__(self):

		self.dr=Base('chrome')
		self.dr.max_window()
		self.dr.open('http://127.0.0.1/wordpress/wp-login.php')


	def login(self,username,password):

		self.dr.clear_element('id=>user_login')
		self.dr.sendkeys('id=>user_login',username)
		self.dr.clear_element('id=>user_pass')
		self.dr.sendkeys('id=>user_pass', password)
		self.dr.get_element("id=>wp-submit").click()

	def get_login_success_text(self):

		return self.dr.get_element_text('css=>#wp-admin-bar-my-account>a')

	def get_login_error_text(self):

		return self.dr.get_element_text('id=>login_error')

	def get_login_success_url(self):
		return self.dr.get_current_url()

	def quit(self):
		self.dr.close()


