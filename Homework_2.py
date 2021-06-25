from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/") #переход по ссылке
driver.find_element_by_name("username").send_keys("admin") #заполнение поля
driver.find_element_by_name("password").send_keys("admin") #заполнение поля
driver.find_element_by_name("login").click() #нажатие на кнопку
driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog") #переход по ссылке
driver.close()