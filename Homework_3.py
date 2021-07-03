from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/")  # переход по ссылке
driver.find_element_by_name("username").send_keys("admin")  # заполнение поля
driver.find_element_by_name("password").send_keys("admin")  # заполнение поля
driver.find_element_by_name("login").click()  # нажатие на кнопку
wait = WebDriverWait(driver,10) # ожидание

menu_number = len(driver.find_elements_by_css_selector("ul#box-apps-menu > li")) # список пунктов меню слева

while menu_number: # цикл для нажатия пунктов меню слева
    menu_number -= 1
    menu_items = driver.find_elements_by_css_selector("ul#box-apps-menu > li")
    menu_items[menu_number].click()

    def are_elements_present(driver, *args): # функция для проверки наличия заголовка
        return len(driver.find_elements(*args)) > 0 # условие, что находится хотя бы один элемент

    are_elements_present(driver, By.TAG_NAME, "h1") > 0 # проверка наличия заголовка

    submenu_number = len(driver.find_elements_by_css_selector(".docs>li>a")) # список вложенных пунктов меню слева

    while submenu_number: # цикл для нажатия вложенных пунктов меню слева
        submenu_number -= 1
        submenu_items = driver.find_elements_by_css_selector(".docs>li>a")
        submenu_items[submenu_number].click()
        are_elements_present(driver, By.TAG_NAME, "h1") > 0 # проверка наличия заголовка во вложенных пунктах


