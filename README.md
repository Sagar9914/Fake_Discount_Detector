# 🛍️ Fake Discount Detector

A web-based application that analyzes product pricing information from **Amazon** and **Flipkart** and identifies potentially misleading discounts using web scraping, data extraction, and rule-based analytics.

## 🚀 Overview

Online shopping platforms often display large discounts that may not accurately represent real savings. This project helps users evaluate product pricing by extracting product information from Amazon or Flipkart product URLs and applying intelligent pricing analysis.

The system automatically detects which platform a link belongs to, extracts product details (including the product image), calculates discount metrics, and generates a verdict indicating whether a deal appears genuine, suspicious, or overpriced.

---

## ✨ Features

* 🔍 Product URL Analysis — works with both **Amazon** and **Flipkart** links
* 🧭 Automatic platform detection (no need to tell it which site the link is from)
* 📦 Automatic Product Information Extraction
* 💰 Current Price & MRP Detection
* 📉 Discount Percentage Calculation
* 🧠 Rule-Based Discount Analysis
* 🖼️ Product Image Display on the result card
* 📊 Interactive, animated Flask Dashboard ("scan report" UI)
* ⚡ Real-Time Processing

---

## 🏗️ System Workflow

```text
Product URL (Amazon or Flipkart)
      ↓
Platform Detection
      ↓
Data Extraction (title, price, MRP, image)
      ↓
Data Cleaning
      ↓
Price Analysis
      ↓
Rule Engine
      ↓
Final Verdict
```

---

## 🛠️ Tech Stack

* Python
* Flask
* Selenium
* BeautifulSoup
* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```text
Fake-Discount-Detector/
│
├── app.py                 # Flask web app (Amazon + Flipkart)
├── main.py                # Command-line version
├── amazon_scraper.py      # Amazon product scraper
├── flipkart_scraper.py    # Flipkart product scraper
├── buyhatke_scraper.py    # Price-history scraper
├── google_search.py       # Buyhatke link builder
├── detector.py            # Rule-based fake-discount logic
├── utils.py               # Cleaning helpers + platform detection
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── logo.png
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/fake-discount-detector.git
cd fake-discount-detector
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** This project uses Selenium with Chrome. Make sure Google Chrome is installed on your machine. Selenium 4.6+ downloads the matching ChromeDriver automatically — if you hit a driver error, install/update Chrome and try again.

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📊 Detection Logic

The application evaluates pricing data using business rules such as:

* Price-to-MRP comparison
* Discount validation
* Suspicious pricing detection
* Overpricing identification
* Deal quality assessment

---

## 🎯 Use Cases

* Online Shopping Assistance
* Price Verification
* E-Commerce Analytics
* Consumer Awareness
* Data Analytics Demonstration

---

## 🔮 Future Enhancements

* Machine Learning-Based Prediction
* Advanced Price Trend Analysis
* More Platforms (Myntra, Ajio, Croma, etc.)
* Browser Extension
* Cloud Deployment

---

## 👨‍💻 Author

**Sagar**

Data Analytics | Python | Web Scraping | Automation | Machine Learning

---

⭐ If you found this project useful, consider giving it a star.
