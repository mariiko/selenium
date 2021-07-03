from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/")  # переход по ссылке
driver.find_element_by_name("username").send_keys("admin")  # заполнение поля
driver.find_element_by_name("password").send_keys("admin")  # заполнение поля
driver.find_element_by_name("login").click()  # нажатие на кнопку
wait = WebDriverWait(driver,10)

menu_number = len(driver.find_elements_by_css_selector("ul#box-apps-menu > li"))

while menu_number:
    menu_number -= 1
    menu_items = driver.find_elements_by_css_selector("ul#box-apps-menu > li")
    menu_items[menu_number].click()

    def are_elements_present(driver, *args):
        return len(driver.find_elements(*args)) > 0

    are_elements_present(driver, By.TAG_NAME, "h1") > 0

    submenu_number = len(driver.find_elements_by_css_selector(".docs>li>a"))

    while submenu_number:
        submenu_number -= 1
        submenu_items = driver.find_elements_by_css_selector(".docs>li>a")
        submenu_items[submenu_number].click()
        are_elements_present(driver, By.TAG_NAME, "h1") > 0


