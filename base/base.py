from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base():

	def __init__(self,browser):

		if browser=="firefox":
			driver=webdriver.Firefox()
		if browser=="chrome":
			driver=webdriver.Chrome()
		try:
			self.browser=browser
			self.driver=driver
		except:
			raise NameError("error browser")

	def open(self,url):

		self.driver.get(url)
		sleep(1)

	def quit(self):
		
		self.driver.quit()

	def close(self):
		self.driver.close()


	def max_window(self):

		self.driver.maximize_window()

	def get_element(self,by,css):
		'''定位元素'''

		if by=="id":
			element=self.driver.find_element_by_id(css)
		elif by=="xpath":
			element=self.driver.find_element_by_xpath(css)
		elif by=="name":
			element=self.driver.find_element_by_name(css)
		elif by=="css":
			element=self.driver.find_element_by_css_selector(css)
		elif by=="link_text":
			element=self.driver.find_element_by_link_text(css)
		elif by=="class":
			element=self.driver.find_element_by_class_name(css)
		else:
			raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
		return element

	def wait_element(self,by,css):
		'''等待元素'''

		for i in range(60):
			try:
				element=self.get_element(by,css)

				if element.is_displayed():
					break;
			except:
				pass
			sleep(1)
		else:
			raise NameError("Please enter the correct targeting elements")

	def element_click(self,by,css):
		'''元素点击'''

		self.wait_element(by,css)
		elemnet=self.get_element(by,css)
		elemnet.click()

	def element_clear(self,by,css):
		'''元素内容清空'''

		self.wait_element(by,css)
		elemnet=self.get_element(by,css)
		elemnet.clear()

	def element_sendkeys(self,by,css,value):
		'''元素内容传值'''

		self.wait_element(by,css)
		element=self.get_element(by,css)
		element.send_keys(value)

	def switch_frame(self,by,css):
		'''切换frame'''

		self.wait_element(by,css)
		element=self.get_element(by,css)
		self.driver.switch_to.frame(element)


	def switch_frame_out(self):
		'''frame out'''

		self.driver.switch_to.default_content()

	def move_to_element(self,by,css):
		'''鼠标悬停'''

		self.wait_element(by,css)
		elemnet=self.get_element(by,css)
		ActionChains(self.driver).move_to_element(elemnet).perform()

	def select_element(self,by,css,value):
		'''下拉框选择'''

		self.wait_element(by,css)
		element=self.get_element(by,css)
		Select(element).select_by_value(value)

	def get_element_attribute(self,by,css):

		self.wait_element(by,css)
		return self.get_element(by,css).get_attribute()

	def get_element_text(self,by,css):

		self.wait_element(by,css)
		return self.get_element(by,css).text

	def get_current_url(self):

		return self.driver.current_url

	def get_element_attribute(self,by,css,attribute):

		self.wait_element(by,css)
		return self.get_element(by,css).get_attribute(attribute)

	def set_richtext(self,by,css,text):

		if by=='id':
			js ='document.getElementById("%s").contentWindow.document.body.innerHTML="%s"' %(css,text)
		elif by=='class':
			js='document.getElementsByClassName("%s")[0].contentWindow.document.body.innerHTML="%s"' %(css,text)
		elif by=='name':
			js='document.getElementsByName("%s")[0].contentWindow.document.body.innerHTML="%s"' %(css,text)
		elif by=='tag':
			js='document.getElementsByTagName("%s")[0].contentWindow.document.body.innerHTML="%s"' %(css,text)
		else:
			raise NameError("Please enter the correct targeting elements.")

		self.driver.execute_script(js)

	def set_scroll_foot(self):

		sleep(1)
		if self.browser=='chrome':
			js='document.body.scrollTop=10000'
		if self.browser=='firefox':
			js='document.documentElement.scrollTop=10000'
		self.driver.execute_script(js)

	def set_scroll_top(self):

		sleep(1)
		if self.browser=='chrome':
			js='document.body.scrollTop=0'
		if self.browser=='firefox':
			js='document.documentElement.scrollTop=0'
		self.driver.execute_script(js)

	def window_scroll_foot(self):

		sleep(1)
		js='window.scrollTo(0,document.body.scrollHeight)'
		self.driver.execute_script(js)

	def window_scroll_top(self):

		sleep(1)
		js='window.scrollTo(0,0)'
		self.driver.execute_script(js)

	def set_date(self,by,css,date):

		if by=='id':
			js ='document.getElementById("%s").removeAttribute("readonly")' %(css)
		elif by=='class':
			js='document.getElementsByClassName("%s")[0].removeAttribute("readonly")' %(css)
		elif by=='name':
			js='document.getElementsByName("%s")[0].removeAttribute("readonly")' %(css)
		elif by=='tag':
			js='document.getElementsByTagName("%s")[0].removeAttribute("readonly")' %(css)
		else:
			raise NameError("Please enter the correct targeting elements.")

		self.driver.execute_script(js)	
		self.element_clear(by, css)
		self.element_sendkeys(by, css, date)


	def send_file(self,by,css,filename):

		self.wait_element(by, css)
		self.get_element(by, css).send_keys(filename)




