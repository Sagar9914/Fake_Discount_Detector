import re

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
    return int(discount.replace("-", "").replace("%", "").strip())

def clean_price_value(value):
    if isinstance(value, str):
        value = value.replace("₹", "").replace(",", "").strip()
        
        try:
            return int(float(value))   
        except:
            return None
    return value