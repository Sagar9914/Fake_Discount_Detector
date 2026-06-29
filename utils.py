import re

def detect_platform(url):
    """
    Looks at the URL and returns 'amazon', 'flipkart' or None
    so app.py knows which scraper to use.
    """
    if not url:
        return None

    url = url.lower()

    if "amazon." in url or "amzn.to" in url or "amzn.in" in url:
        return "amazon"

    if "flipkart." in url or "fkrt.it" in url or "fkrt.co" in url:
        return "flipkart"

    return None

def clean_price(price):
    if not price:
        return None

    price = price.replace(",", "")
    match = re.search(r'\d+', price)

    return int(match.group()) if match else None

def clean_title(title):
    if not title:
        return None
    
    # take only first few words
    words = title.split()
    return " ".join(words[:6])

def clean_discount(discount):
    if not discount:
        return None

    # Pulls the first number out regardless of surrounding text,
    # e.g. "80% off", "-80%", "80 off", "Save 80%" all become 80.
    match = re.search(r'\d+', str(discount))
    return int(match.group()) if match else None

def clean_price_value(value):
    if isinstance(value, str):
        value = value.replace("₹", "").replace(",", "").strip()
        
        try:
            return int(float(value))   
        except:
            return None
    return value