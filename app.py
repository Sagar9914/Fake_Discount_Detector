from flask import Flask, render_template, request
from amazon_scraper import get_product_info as get_amazon_info
from flipkart_scraper import get_product_info as get_flipkart_info
from google_search import find_buyhatke_link
from buyhatke_scraper import get_buyhatke_data
from utils import clean_price, clean_discount, clean_price_value, detect_platform
from detector import detect_fake_discount

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        url = request.form["url"].strip()
        platform = detect_platform(url)

        link = find_buyhatke_link(url)
        
        if platform is None:
            error = "That doesn't look like an Amazon or Flipkart product link. Please paste a valid product URL."
            return render_template("index.html", result=result, error=error)

        try:
            # Pick the right scraper based on the link
            if platform == "amazon":
                data = get_amazon_info(url)
            else:
                data = get_flipkart_info(link)
        except Exception as exc:
            error = f"Couldn't read that product page. The site may have blocked the request or changed its layout. ({exc})"
            return render_template("index.html", result=result, error=error)

        price = clean_price(data.get("price"))
        mrp = clean_price(data.get("mrp"))
        discount = clean_discount(data.get("discount"))
        image = data.get("image")

        if not discount and price and mrp:
            discount = int(((mrp - price) / mrp) * 100)

        # Buyhatke price-history data

        lowest = highest = average = None

        if link:
            try:
                lowest, highest, average = get_buyhatke_data(link)
            except Exception:
                lowest, highest, average = None, None, None

            lowest = clean_price_value(lowest)
            highest = clean_price_value(highest)
            average = clean_price_value(average)

        # Final Result
        final_result = detect_fake_discount(price, mrp, lowest, highest, average)

        result = {
            "platform": platform,
            "title": data.get("title"),
            "image": image,
            "price": price,
            "mrp": mrp,
            "discount": discount,
            "lowest": lowest,
            "highest": highest,
            "average": average,
            "final": final_result
        }

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
