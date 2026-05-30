def detect_fake_discount(price, mrp, lowest_price, Highest_price, Average_price):
    if not price or not mrp:
        return "Not enough data"

    discount = (mrp - price) / mrp * 100

    if discount > 60:
        return "⚠️ Suspicious (High Discount)"

    if mrp > price * 3:
        return "🚨 Fake (MRP inflated)"
    

    if lowest_price and price > lowest_price:
        return "🚨 Fake (Higher than historical)"
    
    # 1. Best deal
    if lowest_price and price <= lowest_price:
        return "🔥 Best Deal (Lowest Price)"

    # 2. Fake discount (price higher than history)
    if lowest_price and price > lowest_price * 1.2:
        return "🚨 Fake Discount"

    # 3. Overpriced
    if Average_price and price > Average_price * 1.15:
        return "⚠️ Overpriced"

    # 4. Fake MRP
    if mrp and Highest_price and mrp > Highest_price * 1.3:
        return "🚨 Fake MRP"

    # 5. Suspicious high discount
    if discount and discount > 60 and lowest_price and price > lowest_price:
        return "🚨 Fake High Discount"

    return "✅ Genuine"
