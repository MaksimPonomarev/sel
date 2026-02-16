import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_abs1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, "input.first[required]").send_keys("enj")
        browser.find_element(By.CSS_SELECTOR, "input.second[required]").send_keys("enj")
        browser.find_element(By.CSS_SELECTOR, "input.third[required]").send_keys("enj")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Congratulations"))
        ans = browser.find_element(By.TAG_NAME, "h1").text


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

        self.assertEqual(ans, "Congratulations! You have successfully registered!")



    def test_abs2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, "input.first[required]").send_keys("enj")
        browser.find_element(By.CSS_SELECTOR, "input.second[required]").send_keys("enj")
        browser.find_element(By.CSS_SELECTOR, "input.third[required]").send_keys("enj")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Congratulations"))
        ans = browser.find_element(By.TAG_NAME, "h1").text


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

        self.assertEqual(ans, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
