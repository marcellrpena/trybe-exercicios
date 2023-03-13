from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from datetime import date

from time import sleep

def main():
    options = Options()
    # options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.get('https://google.com')

    input = browser.find_element(By.TAG_NAME, 'input')
    input.send_keys('1 dólar')
    input.send_keys(Keys.ENTER)

    sleep(1)

    dolar = browser.find_element(By.CSS_SELECTOR, "span.DFlfde.SwHCTb")
    value = dolar.get_attribute('data-value')

    browser.quit()

    with open('dolar.txt', 'a') as file:
        today = date.today().isoformat()
        text_line = f"{today} - {value}\n"
        file.write(text_line)

if __name__ == '__main__':
    main()