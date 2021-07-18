from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import os
import datetime

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
driver.implicitly_wait(10)
driver.find_element_by_css_selector("[href*=catalog]").click()
driver.find_element_by_css_selector("[href*=edit_product]").click()


def test_1():
    driver.find_element_by_css_selector("[value='0'][data-type='toggle']").click()
    driver.find_element_by_name("name[en]").send_keys("name_product")
    driver.find_element_by_name("code").send_keys("code_product")
    driver.find_element_by_css_selector("[data-name='Rubber Ducks']").click()
    driver.find_element_by_css_selector("[value='1-2']").click()
    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys("100")
    Select(driver.find_element_by_name("sold_out_status_id")).select_by_value("2")
    path = os.path.abspath("pic/peace.jpg")
    driver.find_element_by_css_selector("[type='file']").send_keys(path)
    driver.find_element_by_name("date_valid_from").send_keys(datetime.date.today().strftime('%d-%m-%Y'))
    driver.find_element_by_name("date_valid_to").send_keys(
        (datetime.date.today() + datetime.timedelta(days=30)).strftime('%d-%m-%Y'))

    driver.find_element_by_css_selector("[href='#tab-information']").click()
    Select(driver.find_element_by_name("manufacturer_id")).select_by_value("1")
    driver.find_element_by_name("keywords").send_keys("key_words_product")
    driver.find_element_by_name("short_description[en]").send_keys("short_description_product")
    driver.find_element_by_class_name("trumbowyg-editor").send_keys("description_of_product")
    driver.find_element_by_name("head_title[en]").send_keys("head_title_product")
    driver.find_element_by_name("meta_description[en]").send_keys("meta_description_product")

    driver.find_element_by_css_selector("[href='#tab-prices']").click()
    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys("100")
    Select(driver.find_element_by_name("purchase_price_currency_code")).select_by_value("USD")
    driver.find_element_by_css_selector(".input-wrapper [name='prices[USD]']").send_keys("100")
    driver.find_element_by_css_selector(".input-wrapper [name='prices[EUR]']").send_keys("100")
    driver.find_element_by_css_selector("a#add-campaign").click()
    driver.find_element_by_name("campaigns[new_1][start_date]").send_keys(
        datetime.date.today().strftime('%d-%m-%Y') + (Keys.ARROW_RIGHT) + (datetime.datetime.now().strftime('%H:%M')))
    driver.find_element_by_name("campaigns[new_1][end_date]").send_keys(
        (datetime.date.today() + datetime.timedelta(days=30)).strftime('%d-%m-%Y') + (Keys.ARROW_RIGHT) + (
            datetime.datetime.now().strftime('%H:%M')))
    driver.find_element_by_name("campaigns[new_1][percentage]").clear()
    driver.find_element_by_name("campaigns[new_1][percentage]").send_keys("50")

    driver.find_element_by_name("save").click()

    driver.find_element_by_link_text("name_product").click()

    driver.close()
