# 🛍️ Fake Discount Detector

A web-based application that analyzes product pricing information and identifies potentially misleading discounts using web scraping, data extraction, and rule-based analytics.

## 🚀 Overview

Online shopping platforms often display large discounts that may not accurately represent real savings. This project helps users evaluate product pricing by extracting product information from product URLs and applying intelligent pricing analysis.

The system automatically extracts product details, calculates discount metrics, and generates a verdict indicating whether a deal appears genuine, suspicious, or overpriced.

---

## ✨ Features

* 🔍 Product URL Analysis
* 📦 Automatic Product Information Extraction
* 💰 Current Price & MRP Detection
* 📉 Discount Percentage Calculation
* 🧠 Rule-Based Discount Analysis
* 🖼️ Product Image Display
* 📊 Interactive Flask Dashboard
* ⚡ Real-Time Processing

---

## 🏗️ System Workflow

```text
Product URL
      ↓
Data Extraction
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
├── app.py
├── amazon_scraper.py
├── detector.py
├── utils.py
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
* Multi-Platform Product Support
* Browser Extension
* Cloud Deployment

---

## 👨‍💻 Author

**Sagar**

Data Analytics | Python | Web Scraping | Automation | Machine Learning

---

⭐ If you found this project useful, consider giving it a star.
