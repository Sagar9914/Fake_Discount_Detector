from amazon_scraper import get_product_info
from google_search import find_buyhatke_link
from buyhatke_scraper import get_buyhatke_data
from utils import clean_price, clean_discount, clean_price_value
from detector import detect_fake_discount

def run():
    product_url = input("Enter Amazon Product URL: ")

    print("\nFetching Amazon data...")
    data = get_product_info(product_url)

    print("Product:", data["title"])

    price = clean_price(data["price"])
    mrp = clean_price(data["mrp"])

    print("Price:", price)
    print("MRP:", mrp)

    discount = clean_discount(data["discount"])
    if not discount and price and mrp:
        discount = int(((mrp - price) / mrp) * 100)

    print("Discount:", discount, "%")

    print("\nSearching Buyhatke...")
    link = find_buyhatke_link(product_url)

    

    if link:
        print("Buyhatke Link:", link)
        lowest_price, Highest_price, Average_price = get_buyhatke_data(link)
        
    else:
        print("No Buyhatke link found")
        lowest_price, Highest_price, Average_price = None

    lowest_price = clean_price_value(lowest_price)
    Highest_price = clean_price_value(Highest_price)
    Average_price = clean_price_value(Average_price)
        

    print("Lowest Price:", lowest_price)
    print("Highest Price:", Highest_price)
    print("Average Price:", Average_price)

    result = detect_fake_discount(price, mrp, lowest_price, Highest_price, Average_price)

    print("\nFINAL RESULT:", result)

if __name__ == "__main__":
    run()