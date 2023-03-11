from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import os
import requests


def find_gifs():
    figs = browser.find_elements(By.CLASS_NAME, "GifListItem")
    gifs = {}
    for fig in figs:
        try:
            idx = fig.get_attribute("data-index")
            gif = fig.find_element(By.TAG_NAME, "img")
            url = gif.get_attribute("src")
            gifs[idx] = url
        except (WebDriverException, AttributeError):
            pass
    return gifs


def save_gif(idx, url):
    if not os.path.isdir("tenor"):
        os.mkdir("tenor")

    with open(f"./tenor/{idx}.gif", "wb") as file:
        # stream=True means 'don't load all at once'
        res = requests.get(url, stream=True)
        # get at most X bytes at a time
        for block in res.iter_content(1024):
            if block:
                file.write(block)


if __name__ == "__main__":
    options = Options()
    # Uncomment the line bellow to make the browser "headless" (hidden)
    # options.add_argument('--headless')

    browser = webdriver.Firefox(options=options)
    browser.get("https://tenor.com")

    saved = set()
    MAX_SAVE = 50

    while len(saved) < MAX_SAVE:
        curr = find_gifs()

        for idx, url in curr.items():
            if idx not in saved:
                print(f'+ Saving {idx}')
                save_gif(idx, url)
                saved.add(idx)
            else:
                print(f'  Skipping {idx}')

        browser.execute_script("window.scrollBy(0, 150)")

    browser.quit()
