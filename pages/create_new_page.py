import sys
sys.path.append('../')
from base.base import Base

class CreateNewPage():

	def __init__(self):

		self.dr=Base("chrome")
		self.dr.max_window()

	def login_as_admin(self,username,password):

		self.dr.open('http://127.0.0.1/wordpress/wp-login.php')
		self.dr.element_clear('id','user_login')
		self.dr.element_sendkeys('id','user_login',username)
		self.dr.element_clear('id','user_pass')
		self.dr.element_sendkeys('id','user_pass', password)
		self.dr.element_click('id','wp-submit')

	def open_post_new(self):

		url=self.dr.get_element_attribute('css','.welcome-icon.welcome-write-blog', 'href')
		self.dr.open(url)

	def set_title(self,title):

		self.dr.element_sendkeys('id','title',title)

	def set_content(self,text):

		self.dr.set_richtext('id','content_ifr',text)

	def publish(self):

		self.dr.element_click('id','publish')

	def quit(self):

		self.dr.close()

