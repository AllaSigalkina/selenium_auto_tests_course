from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

y_element = browser.find_element(By.ID, "answer")
y_element.send_keys(y)

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

time.sleep(15)
