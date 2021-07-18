from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 1.5)
driver.implicitly_wait(1.5)
driver.get("http://localhost/litecart/en/")


def test_add_products_to_cart():
    for i in range(3):
        driver.find_element_by_css_selector("#box-most-popular ul :first-child a.link").click()
        if len(driver.find_elements_by_css_selector("[name='options[Size]']")) == 1:
            Select(driver.find_element_by_name("options[Size]")).select_by_value("Small")
        driver.find_element_by_name("add_cart_product").click()
        counter = int(driver.find_element_by_css_selector("span.quantity").text)
        wait.until(lambda s: int(s.find_element_by_css_selector("span.quantity").text) == counter + 1)
        driver.back()

    driver.find_element_by_css_selector("[href*='checkout'].link").click()
    numbers_of_products = len(driver.find_elements_by_css_selector("table.dataTable tr"))
    while numbers_of_products > 0:
        driver.find_element_by_name("remove_cart_item").click()
        WebDriverWait(driver, 10).until(lambda s: len(s.find_elements_by_css_selector("table.dataTable tr")) < numbers_of_products)
        numbers_of_products = len(driver.find_elements_by_css_selector("table.dataTable tr"))
    driver.back()

    driver.close()