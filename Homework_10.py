from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("http://localhost/litecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
driver.implicitly_wait(10)
driver.find_element_by_css_selector("#box-apps-menu [href*=countries]").click()
driver.find_element_by_css_selector(".dataTable [href*=AU]").click()
main_window = driver.current_window_handle


def test_open_windows():
    all_links = driver.find_elements_by_css_selector("[class='fa fa-external-link']")

    for link in all_links:
        existingWindows = driver.window_handles
        link.click()
        new_existingWindows = driver.window_handles
        new_window = list(set(existingWindows) ^ set(new_existingWindows))
        wait.until(ec.new_window_is_opened(new_window))
        print(new_window)

        for item in new_window:
            print(item)
            driver.switch_to.window(item)
            driver.close()
        driver.switch_to.window(main_window)



