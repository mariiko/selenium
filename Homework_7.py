import random
import string
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


def random_string(item, len):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(len)])


def test_1():
    create_account = dict(
        firstname="Ivan",
        lastname="Ivanov",
        address1="Street_1",
        postcode="12345",
        city="Saint-Petersburg",
        email=random_string("", 10) + "@gmail.com",
        phone="+71234567890",
        password="12345",
        confirmed_password="12345"
    )

    driver.get("http://localhost/litecart/")
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("[name=login_form] a ").click()

    for key, item in create_account.items():
        driver.find_element_by_name(key).send_keys(item)

    Select(driver.find_element_by_css_selector("[name=country_code]")).select_by_value("US")
    Select(driver.find_element_by_css_selector("select[name = zone_code]")).select_by_value("AL")
    driver.find_element_by_css_selector("[name=create_account]").click()

    driver.find_element_by_css_selector("#box-account :nth-child(4) a").click()

    driver.find_element_by_css_selector("[name=email]").send_keys(create_account["email"])
    driver.find_element_by_css_selector("[name=password]").send_keys(create_account["password"])
    driver.find_element_by_css_selector("[name=login]").click()
    driver.find_element_by_css_selector("#box-account [href$='/logout']").click()

    driver.close()