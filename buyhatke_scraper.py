from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_buyhatke_data(url):

    chrome_options = Options()
    chrome_options.add_argument("--headless")   # 🔥 RUN IN BACKGROUND
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    time.sleep(5)

    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(3)

    lowest = highest = average = None

    try:
        lowest = driver.find_element(By.XPATH, "//*[contains(text(),'Lowest')]/following::span").text
    except:
        pass

    try:
        highest = driver.find_element(By.XPATH, "//*[contains(text(),'Highest')]/following::span").text
    except:
        pass

    try:
        average = driver.find_element(By.XPATH, "//*[contains(text(),'Average')]/following::span").text
    except:
        pass

    driver.quit()

    return lowest, highest, average