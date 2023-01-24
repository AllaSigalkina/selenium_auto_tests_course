from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:

    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text

    z = int(x) + int(y)
    z_str = str(z)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    num = select.select_by_value(z_str)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла