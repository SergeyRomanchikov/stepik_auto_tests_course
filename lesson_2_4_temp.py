
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time 
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '100')
        )
    book_button = browser.find_element_by_id("book")
    book_button.click()


    x_element = browser.find_element_by_xpath("//span[@id = 'input_value']")
    x = int(x_element.text)



    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    expression = calc(x)

    text_area_element = browser.find_element_by_xpath("//input[@id = 'answer']")
    text_area_element.send_keys(expression)

    submit_button = browser.find_element_by_xpath("//button[@type = 'submit']")
    submit_button.click()
    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла