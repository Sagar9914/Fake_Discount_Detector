from flask import Flask, render_template, request
from amazon_scraper import get_product_info
from google_search import find_buyhatke_link
from buyhatke_scraper import get_buyhatke_data
from utils import clean_price, clean_discount, clean_price_value
from detector import detect_fake_discount

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        url = request.form["url"]

        # Amazon Data
        data = get_product_info(url)

        price = clean_price(data["price"])
        mrp = clean_price(data["mrp"])
        discount = clean_discount(data["discount"])

        if not discount and price and mrp:
            discount = int(((mrp - price) / mrp) * 100)

        # Buyhatke Data
        link = find_buyhatke_link(url)

        lowest = highest = average = None

        if link:
            lowest, highest, average = get_buyhatke_data(link)

            lowest = clean_price_value(lowest)
            highest = clean_price_value(highest)
            average = clean_price_value(average)

        # Final Result
        final_result = detect_fake_discount(price, mrp, lowest, highest, average)

        result = {
            "title": data["title"],
            "price": price,
            "mrp": mrp,
            "discount": discount,
            "lowest": lowest,
            "highest": highest,
            "average": average,
            "final": final_result
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)