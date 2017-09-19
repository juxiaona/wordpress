import sys 
sys.path.append("../")

from pages.create_new_page import CreateNewPage
import unittest


class CreateNew(unittest.TestCase):

	def setUp(self):

		self.create_new=CreateNewPage()

	def tearDown(self):

		self.create_new.quit()

	def test_create_new(self):

		self.create_new.login_as_admin('admin', 'jxn461028')
		self.create_new.open_post_new()
		self.create_new.set_title('test')
		self.create_new.set_content('1234567')
		self.create_new.publish()

if __name__ == '__main__':
	
	unittest.main()