import sys
sys.path.append("../")
from base.base import Base

class LoginPage():

	def __init__(self):

		self.dr=Base('chrome')
		self.dr.max_window()
		self.dr.open('http://127.0.0.1/wordpress/wp-login.php')


	def login(self,username,password):

		self.dr.element_clear('id','user_login')
		self.dr.element_sendkeys('id','user_login',username)
		self.dr.element_clear('id','user_pass')
		self.dr.element_sendkeys('id','user_pass', password)
		self.dr.element_click('id','wp-submit')

	def get_login_success_text(self):

		return self.dr.get_element_text('css','#wp-admin-bar-my-account>a')

	def get_login_error_text(self):

		return self.dr.get_element_text('id','login_error')

	def get_login_success_url(self):
		return self.dr.get_current_url()

	def quit(self):
		self.dr.close()


