from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://guanjia.xxkuaipao.com/login")
driver.find_element_by_id('frc-name-1088').send_keys('ppytest')
driver.find_element_by_id('frc-pwd-1088').send_keys('ppy123')
driver.find_element_by_class_name('submit').click()

sleep(1)
driver.get('https://guanjia.xxkuaipao.com/user/list')
driver.find_element_by_link_text('添加会员').click()

driver.find_element_by_class_name('wrap-image-upload').send_keys('../data/1.jpg')
driver.quit()