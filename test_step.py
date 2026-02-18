import time
from dataclasses import field

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import math


def ans():
    return math.log(int(time.time()))


@pytest.mark.parametrize("link",[
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_login(browser, link):
    browser.get(link)

    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "id_login_email"))).send_keys("ponomarevmaksim989@gmail.com")
    wait.until(EC.element_to_be_clickable((By.ID, "id_login_password"))).send_keys("(-maksiM1234-)")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    wait.until(EC.invisibility_of_element_located((By.ID, "id_login_email")))
    try:
        again = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn.white")))
        again.click()
    except:
        print("Кнопка 'Решить снова' не найдена, идем дальше")

    field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea.string-quiz__textarea")))

    answer = str(ans())

    field.send_keys(answer)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))).click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    text_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    text = text_element.text

    assert text == "Correct!", f"Ожидалось 'Correct', а вышло {text}"