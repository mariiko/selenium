from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge("msedgedriver.exe")#обратилась напрямую к файлу, т.к. по-другому не работало

driver.get("http://localhost/litecart/en/")  # переход по ссылке
wait = WebDriverWait(driver, 10)  # ожидание


first_duck = driver.find_element_by_css_selector("#box-campaigns a") #ищем первый элемент блоке Campaigns
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
assert(first_duck_regular_price_colour == "rgba(119, 119, 119, 1)" or "rgba(119, 119, 119)")
print("Цвет текста обычной цены первой утки совпадает")
first_duck_regular_price_crossed_out = driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("text-decoration-line")
assert(first_duck_regular_price_crossed_out == "line-through")
print("Обычная цена первой утки зачеркнута")
first_duck.click()
second_duck_regular_price_colour = driver.find_element_by_css_selector(".price-wrapper .regular-price").value_of_css_property("color")
assert(second_duck_regular_price_colour == "rgba(102, 102, 102, 1)" or "rgba(102, 102, 102)")
print("Цвет текста обычной цены второй утки совпадает")
second_duck_regular_price_crossed_out = driver.find_element_by_css_selector(".price-wrapper .regular-price").value_of_css_property("text-decoration-line")
assert(second_duck_regular_price_crossed_out == "line-through")
print("Обычная цена второй утки зачеркнута")
driver.back()

first_duck = driver.find_element_by_css_selector("#box-campaigns .campaign-price")
first_duck_campaign_price_colour = driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("color")
assert(first_duck_campaign_price_colour == "rgba(204, 0, 0, 1)" or "rgba(204, 0, 0)")
print("Цвет текста акционной цены первой утки совпадает")
first_duck_campaign_price_weight = driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("font-weight")
assert(first_duck_campaign_price_weight == "700" or "900")
print("Жирность текста акционной цены первой утки совпадает")
first_duck.click()
second_duck_campaign_price_colour = driver.find_element_by_css_selector(".price-wrapper .campaign-price").value_of_css_property("color")
assert(second_duck_campaign_price_colour == "rgba(204, 0, 0, 1)" or "rgba(204, 0, 0)")
print("Цвет текста акционной цены второй утки совпадает")
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