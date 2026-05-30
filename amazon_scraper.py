from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def get_product_info(url):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(5)

    # Scroll to load price
    driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(3)

    # Title
    try:
        title = driver.find_element(By.ID, "productTitle").text.strip()
    except:
        title = None

    # ✅ PRICE (ROBUST)
    price = None
    price_selectors = [
        "//span[@class='a-price-whole']",
        "//span[@id='priceblock_ourprice']",
        "//span[@id='priceblock_dealprice']",
        "(//span[contains(text(),'₹')])[1]"
    ]

    for sel in price_selectors:
        try:
            price = driver.find_element(By.XPATH, sel).text
            if price:
                break
        except:
            continue

# ✅ DISCOUNT (from Amazon UI)
    discount = None

    discount_selectors = [
        "//span[contains(text(),'%')]",
        "//span[contains(@class,'savingsPercentage')]",
        ]

    for sel in discount_selectors:
        try:
           discount = driver.find_element(By.XPATH, sel).text
           if discount:
                break
        except:
            continue

    # ✅ MRP
    mrp = None
    mrp_selectors = [
        "//span[.='M.R.P.']/following::span[1]",
        "//span[contains(text(),'M.R.P')]/following::span[1]",
        "//span[@class='a-price a-text-price']//span[@class='a-offscreen']",
        "(//span[contains(text(),'₹')])[2]"
        ]
    for sel in mrp_selectors:
        try:
            mrp = driver.find_element(By.XPATH, sel).text
            if mrp:
                break
        except:
            continue


    driver.quit()

    return {
        "title": title,
        "price": price,
        "mrp": mrp,
        "discount" : discount
    }