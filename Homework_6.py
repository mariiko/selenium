from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge("msedgedriver.exe")

driver.get("http://localhost/litecart/en/")
wait = WebDriverWait(driver, 10)


first_duck = driver.find_element_by_css_selector("#box-campaigns a")
first_duck_name = driver.find_element_by_css_selector("#box-campaigns .name").text
first_duck.click()
second_duck_name = driver.find_element_by_css_selector("h1.title").text
if first_duck_name == second_duck_name:
    print("Имена уток совпадают")
else:
    print("Имена уток не совпадают")
driver.back()

first_duck = driver.find_element_by_css_selector("#box-campaigns a")
first_duck_regular_price = driver.find_element_by_css_selector("#box-campaigns .regular-price").text
first_duck_campaign_price = driver.find_element_by_css_selector("#box-campaigns .campaign-price").text
first_duck.click()
second_duck_regular_price = driver.find_element_by_css_selector(".price-wrapper .regular-price").text
second_duck_campaign_price = driver.find_element_by_css_selector(".price-wrapper .campaign-price").text
if first_duck_regular_price == second_duck_regular_price and first_duck_campaign_price == second_duck_campaign_price:
    print("Цены уток совпадают")
else:
    print("Цены уток не совпадают")
driver.back()

first_duck = driver.find_element_by_css_selector("#box-campaigns a")
first_duck_regular_price_colour = driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("color")
first_duck_regular_1 = (first_duck_regular_price_colour.replace("(", " "))
first_duck_regular_2 = first_duck_regular_1.replace(")", "")
first_duck_regular_3 = first_duck_regular_2.replace(",", "")
first_duck_regular_total = first_duck_regular_3.split()
assert(first_duck_regular_total[1] == first_duck_regular_total[2] == first_duck_regular_total[3])
print("Цвет текста обычной цены первой утки серый")

first_duck_regular_price_crossed_out = driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("text-decoration-line")
assert(first_duck_regular_price_crossed_out == "line-through")
print("Обычная цена первой утки зачеркнута")

first_duck.click()
second_duck_regular_price_colour = driver.find_element_by_css_selector(".price-wrapper .regular-price").value_of_css_property("color")
second_duck_regular_1 = (second_duck_regular_price_colour.replace("(", " "))
second_duck_regular_2 = second_duck_regular_1.replace(")", "")
second_duck_regular_3 = second_duck_regular_2.replace(",", "")
second_duck_regular_total = second_duck_regular_3.split()
assert(second_duck_regular_total[1] == second_duck_regular_total[2] == second_duck_regular_total[3])
print("Цвет текста обычной цены второй утки серый")

second_duck_regular_price_crossed_out = driver.find_element_by_css_selector(".price-wrapper .regular-price").value_of_css_property("text-decoration-line")
assert(second_duck_regular_price_crossed_out == "line-through")
print("Обычная цена второй утки зачеркнута")

driver.back()
first_duck = driver.find_element_by_css_selector("#box-campaigns .campaign-price")
first_duck_campaign_price_colour = driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("color")
first_duck_campaign_1 = (first_duck_campaign_price_colour.replace("(", " "))
first_duck_campaign_2 = first_duck_campaign_1.replace(")", "")
first_duck_campaign_3 = first_duck_campaign_2.replace(",", "")
first_duck_campaign_total = first_duck_campaign_3.split()
assert("0" == first_duck_campaign_total[2] == first_duck_campaign_total[3])
print("Цвет текста акционной цены первой утки красный")

first_duck_campaign_price_weight = driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("font-weight")
assert(first_duck_campaign_price_weight == "700" or "900")
print("Жирность текста акционной цены первой утки совпадает")

first_duck.click()
second_duck_campaign_price_colour = driver.find_element_by_css_selector(".price-wrapper .campaign-price").value_of_css_property("color")
second_duck_campaign_1 = (second_duck_campaign_price_colour.replace("(", " "))
second_duck_campaign_2 = second_duck_campaign_1.replace(")", "")
second_duck_campaign_3 = second_duck_campaign_2.replace(",", "")
second_duck_campaign_total = second_duck_campaign_3.split()
assert("0" == second_duck_campaign_total[2] == second_duck_campaign_total[3])
print("Цвет текста акционной цены второй утки красный")

second_duck_campaign_price_weight = driver.find_element_by_css_selector(".price-wrapper .campaign-price").value_of_css_property("font-weight")
assert(second_duck_campaign_price_weight == "700")
print("Жирность текста акционной цены второй утки совпадает")

driver.back()

first_duck = driver.find_element_by_css_selector("#box-campaigns .campaign-price")
first_duck_regular_price_size = driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("font-size")
first_duck_campaign_price_size = driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("font-size")
for_compare_1_1 = (first_duck_regular_price_size[:-2])
for_compare_1_2 = (first_duck_campaign_price_size[:-2])
assert(float(for_compare_1_1) < float(for_compare_1_2))
print("Акционная цена крупнее, чем обычная у первой утки")

first_duck.click()
second_duck_regular_price_size = driver.find_element_by_css_selector(".price-wrapper .regular-price").value_of_css_property("font-size")
second_duck_campaign_price_size = driver.find_element_by_css_selector(".price-wrapper .campaign-price").value_of_css_property("font-size")
for_compare_2_1 = (second_duck_regular_price_size[:-2])
for_compare_2_2 = (second_duck_campaign_price_size[:-2])
assert(float(for_compare_2_1) < float(for_compare_2_2))
print("Акционная цена крупнее, чем обычная у второй утки")

driver.close()