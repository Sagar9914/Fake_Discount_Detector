"""
flipkart_scraper.py

Despite the filename, this does NOT scrape Flipkart.com directly — Flipkart's
bot detection blocks plain Selenium too unreliably to be worth fighting.

Instead, for a Flipkart product, we already redirect through Buyhatke's
price-history page (same URL buyhatke_scraper.py uses), and that page also
displays the product's title, current price, MRP, discount, and image.

Single responsibility: extract title / price / mrp / discount / image
from that Buyhatke page. Price HISTORY (lowest/highest/average) is
deliberately NOT handled here — that's buyhatke_scraper.py's job.
"""

import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

DEBUG = True
PAGE_READY_TIMEOUT = 8
SELECTOR_TIMEOUT = 3


def _build_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    return driver


def _wait_for_page_ready(driver):
    try:
        WebDriverWait(driver, PAGE_READY_TIMEOUT).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    except TimeoutException:
        pass


def _first_match(driver, selectors, attr=None, timeout=SELECTOR_TIMEOUT):
    for i, selector in enumerate(selectors):
        wait_time = timeout if i == 0 else 0.5
        try:
            el = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, selector))
            )
            value = el.get_attribute(attr) if attr else el.text
            value = (value or "").strip()
            if value:
                return value
        except TimeoutException:
            continue
        except Exception:
            continue
    return None


def clean_discount(discount_text):
    """Pull the first integer out of messy discount text like '80% off', '80 off', '-80%'."""
    if not discount_text:
        return None
    match = re.search(r"\d+", discount_text)
    return int(match.group()) if match else None


def _save_debug(driver, label="flipkart"):
    if not DEBUG:
        return
    try:
        driver.save_screenshot(f"{label}_debug.png")
        with open(f"{label}_debug.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print(f"[flipkart_scraper] DEBUG: saved {label}_debug.png / {label}_debug.html")
    except Exception as e:
        print(f"[flipkart_scraper] DEBUG: failed to save debug artifacts: {e}")


def get_product_info(buyhatke_url, driver=None):
    """
    Extract title / price / mrp / discount / image from a Buyhatke page.

    Param `buyhatke_url`: the Buyhatke redirect URL for the Flipkart product
    (e.g. "https://www.buyhatke.com/ https://www.flipkart.com/...").

    Optional `driver`: pass an already-created, already-navigated Selenium
    driver (e.g. one buyhatke_scraper.py already opened for the same URL) to
    avoid a second browser session. If omitted, this function opens and
    closes its own driver — fully standalone, just slower if you're also
    calling buyhatke_scraper.py for the same link.
    """
    owns_driver = driver is None
    if owns_driver:
        driver = _build_driver()
        driver.get(buyhatke_url)
        _wait_for_page_ready(driver)

    title = price = mrp = discount_text = image = None

    try:
        title_selectors = [
            "//h1",
            "//*[contains(@class,'title')][1]",
        ]
        title = _first_match(driver, title_selectors)

        price_selectors = [
            "//*[contains(@class,'price')][contains(text(),'₹')]",
            "(//*[contains(text(),'₹')])[1]",
        ]
        price = _first_match(driver, price_selectors)

        mrp_selectors = [

        # crossed-out prices
        "//del[contains(text(),'₹')]",
        "//s[contains(text(),'₹')]",
        "//strike[contains(text(),'₹')]",

        # line-through style
        "//span[contains(@style,'line-through')]",
        "//*[contains(@class,'line-through')]",

        # labels
        "//*[contains(text(),'MRP')]/following::*[contains(text(),'₹')][1]",
        "//*[contains(text(),'M.R.P')]/following::*[contains(text(),'₹')][1]",
        "//*[contains(text(),'Retail Price')]/following::*[contains(text(),'₹')][1]",
        "//*[contains(text(),'Original Price')]/following::*[contains(text(),'₹')][1]",

        # second ₹ on page (often MRP)
        "(//*[contains(text(),'₹')])[2]"
        ]

        
        mrp = _first_match(driver, mrp_selectors)

        discount_selectors = [
            "//*[contains(text(),'% off')]",
            "//*[contains(text(),'%')]",
        ]
        discount_text = _first_match(driver, discount_selectors)

        image_selectors = [
            "//img[contains(@alt,'product') or contains(@class,'product')]",
            "//img",
        ]
        image = _first_match(driver, image_selectors, attr="src")

        if not title and not price:
            _save_debug(driver, "flipkart")

    except Exception as e:
        print(f"[flipkart_scraper] Error: {e}")
        _save_debug(driver, "flipkart")
    finally:
        if owns_driver:
            driver.quit()

    return {
        "title": title,
        "price": price,
        "mrp": mrp,
        "discount": clean_discount(discount_text),
        "image": image,
    }
