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

	def get_element(self,css):
		'''定位元素'''

		if "=>"not in css:
			raise NameError("Positioning syntax errors, lack of '=>'.")

		by=css.split('=>')[0]
		value=css.split('=>')[1]

		if by=="id":
			element=self.driver.find_element_by_id(value)
		elif by=="xpath":
			element=self.driver.find_element_by_xpath(value)
		elif by=="name":
			element=self.driver.find_element_by_name(value)
		elif by=="css":
			element=self.driver.find_element_by_css_selector(value)
		elif by=="link_text":
			element=self.driver.find_element_by_link_text(value)
		elif by=="class":
			element=self.driver.find_element_by_class_name(value)
		else:
			raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
		return element

	def wait_element(self,css):
		'''等待元素'''

		for i in range(60):
			try:
				element=self.get_element(css)

				if element.is_displayed():
					break;
			except:
				pass
			sleep(1)
		else:
			raise NameError("Please enter the correct targeting elements")

	def click_element(self,css):
		'''元素点击'''

		self.wait_element(css)
		elemnet=self.get_element(css)
		elemnet.click()

	def clear_element(self,css):
		'''元素内容清空'''

		self.wait_element(css)
		elemnet=self.get_element(css)
		elemnet.clear()

	def sendkeys(self,css,text):
		'''元素内容传值'''

		self.wait_element(css)
		element=self.get_element(css)
		element.send_keys(text)

	def switch_frame(self,css):
		'''切换frame'''

		self.wait_element(css)
		element=self.get_element(css)
		self.driver.switch_to.frame(element)


	def switch_frame_out(self):
		'''frame out'''

		self.driver.switch_to.default_content()

	def move_to_element(self,css):
		'''鼠标悬停'''

		self.wait_element(css)
		elemnet=self.get_element(css)
		ActionChains(self.driver).move_to_element(elemnet).perform()

	def select_element(self,css,value):
		'''下拉框选择'''

		self.wait_element(css)
		element=self.get_element(css)
		Select(element).select_by_value(value)

	def get_element_attribute(self,css):

		self.wait_element(css)
		return self.get_element(css).get_attribute()

	def get_element_text(self,css):

		self.wait_element(css)
		return self.get_element(css).text

	def get_current_url(self):

		return self.driver.current_url

	def get_element_attribute(self,css,name):

		self.wait_element(css)
		return self.get_element(css).get_attribute(name)

	def set_content(self,by_id,text):

		js ='document.getElementById("%s").contentWindow.document.body.innerHTML="%s"' %(by_id,text)
		self.driver.execute_script(js)