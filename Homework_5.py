import selenium
from selenium.webdriver.support.wait import WebDriverWait

driver = selenium.webdriver.Chrome()
driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")  # переход по ссылке
driver.find_element_by_name("username").send_keys("admin") #заполнение поля
driver.find_element_by_name("password").send_keys("admin") #заполнение поля
driver.find_element_by_name("login").click() #нажатие на кнопку
wait = WebDriverWait(driver, 10)  # ожидание


countries = driver.find_elements_by_css_selector("tr.row a:not([title])") #ищем все элементы с названием стран
country_name = [] #создаем пустой список имен стран
for country in countries:
    name = country.get_attribute("textContent") #вытаскиваем свойство элемента, содержащее название страны
    country_name.append(name) #добавляем в список имен стран
print(country_name) #проверка, что выводится строка со списком имён стран
if (country_name == sorted(country_name)):# проверяем, что страны расположены в алфавитном порядке
    print("Страны в алфавитном порядке")
else:
    print("Страны не в алфавитном порядке")

not_zero_zones = len(driver.find_elements_by_css_selector(".row td:nth-child(6)"))
print(not_zero_zones)
x = -1
while x < (not_zero_zones-1):
    print(x)
    zone_items = (driver.find_elements_by_css_selector(".row td:nth-child(6)"))
    countries = driver.find_elements_by_css_selector("tr.row a:not([title])")
    x += 1
    if zone_items[x].text != "0":
        countries[x].click()
        zones = driver.find_elements_by_css_selector(".dataTable td:nth-child(3)")  # ищем все элементы с названием зон
        print(zones)
        zone_name = []
        for zone in zones:
            name_z = zone.text  # вытаскиваем свойство элемента, содержащее название зоны
            if zone.text != "":
                zone_name.append(name_z)  # добавляем в список имен зон
        print(zone_name)
        if (zone_name == sorted(zone_name)) :  # проверяем, что зоны расположены в алфавитном порядке
            print("Зоны в алфавитном порядке")
        else:
            print("Зоны не в алфавитном порядке")
        driver.back()


driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
y = 0
while y < len(driver.find_elements_by_css_selector(".row td:nth-child(3)>a")):
    geo_zone_items = (driver.find_elements_by_css_selector(".row td:nth-child(3)>a"))
    geo_zone_items[y].click()
    geo_zones = driver.find_elements_by_css_selector("td:nth-child(3)>select option[selected]")
    name_geo_zones = []
    for geo_zone in geo_zones:
        name_geo_z = geo_zone.text
        name_geo_zones.append(name_geo_z)
    if (name_geo_zones == sorted(name_geo_zones)):
        print("Гео зоны в алфавитном порядке")
    else:
        print("Гео зоны не в алфавитном порядке")
    y += 1
    driver.back()

driver.close()