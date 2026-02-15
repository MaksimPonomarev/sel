from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


file = r"C:\Users\mr\Desktop\test3.txt"

def result(x):
    x = int(x)
    return math.log(abs(12 * math.sin(x)))

#
# def name():
#     try:
#         link = "https://suninjuly.github.io/file_input.html"
#         browser = webdriver.Chrome()
#         browser.get(link)
#
#         browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("enj")
#         browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("enj")
#         browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("enj")
#         browser.find_element(By.ID, "file").send_keys(file)
#         browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#         time.sleep(5)
#         alert = browser.switch_to.alert
#         alert.accept()
#
#     finally:
#         # ожидание чтобы визуально оценить результаты прохождения скрипта
#         time.sleep(10)
#         # закрываем браузер после всех манипуляций
#         browser.quit()
#
#
# def check():
#     try:
#         link = "https://suninjuly.github.io/execute_script.html"
#         browser = webdriver.Chrome()
#         browser.get(link)
#
#         # Ваш код, который заполняет обязательные поля
#
#         x = int(browser.find_element(By.ID, "input_value").text)
#         y = result(x)
#         browser.find_element(By.ID, "answer").send_keys(y)
#         browser.execute_script("window.scrollBy(0, 200);")
#         robot_check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#         robot_check.click()
#
#         robot_check = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#         robot_check.click()
#
#         # Отправляем заполненную форму
#         button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#         button.click()
#
#         # Проверяем, что смогли зарегистрироваться
#         # ждем загрузки страницы
#     finally:
#         # ожидание чтобы визуально оценить результаты прохождения скрипта
#         time.sleep(10)
#         # закрываем браузер после всех манипуляций
#         browser.quit()
#
#
#
# name()


# def alert():
#     try:
#         link = "http://suninjuly.github.io/redirect_accept.html"
#         browser = webdriver.Chrome()
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "button").click()
#
#         new_window = browser.window_handles[1]
#         browser.switch_to.window(new_window)
#
#
#         # browser.find_element(By.CSS_SELECTOR, "button").click()
#         # alert = browser.switch_to.alert
#         # alert.accept()
#         x = browser.find_element(By.ID, "input_value").text
#         res = result(x)
#         browser.find_element(By.ID, "answer").send_keys(res)
#         browser.find_element(By.CSS_SELECTOR, "button").click()
#
#     finally:
#         time.sleep(10)
#         browser.quit()



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()
    x = int(browser.find_element(By.ID, "input_value").text)
    y = result(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(10)
    browser.quit()