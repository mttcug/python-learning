from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
input = driver.find_element_by_css_selector('#kw')
input.send_keys('向日葵图片')

button = driver.find_element_by_css_selector('#su')
button.click()