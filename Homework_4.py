import selenium
from selenium.webdriver.support.wait import WebDriverWait

driver = selenium.webdriver.Chrome()
driver.get("http://localhost/litecart/en/")  # переход по ссылке
wait = WebDriverWait(driver, 10)  # ожидание

ducks_number = (driver.find_elements_by_css_selector(".image-wrapper"))  # список уток

for duck_number in ducks_number:  # цикл для каждой утки

    stickers = duck_number.find_elements_by_css_selector("*.sticker") #поиск стикера в определенной утке
    print(stickers) #проверка для себя

    def are_elements_present(): # функция для проверки наличия стикера
        return len(stikers) == 1 # условие, что находится один элемент

    if not are_elements_present:  # если условие не выполнится
        print("Mistake") #выдать ошибку
        exit(-1) #завершить цикл
    else:
        print("Ok")

driver.close()
