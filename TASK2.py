import csv

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 200
}

def get_user_portfolio():
    portfolio = {}
    print("Enter your stock holdings. Type 'done' to finish.\n")
    while True:
        stock = input("Stock symbol: ").strip().upper()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print(f"'{stock}' is not in the available stock list.")
            continue
        try:
            qty = int(input(f"Enter quantity for {stock}: "))
            if qty < 0:
                print("Quantity must be non-negative.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("Please enter a valid number.")
    return portfolio

def calculate_total(portfolio):
    total = 0
    for stock, qty in portfolio.items():
        total += STOCK_PRICES[stock] * qty
    return total

def display_portfolio(portfolio):
    print("\n📊 Portfolio Summary:")
    print("-" * 40)
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        total_value = price * qty
        print(f"{stock}: {qty} shares x ${price} = ${total_value}")
    print("-" * 40)
    print(f"Total Investment Value: ${calculate_total(portfolio)}\n")

def save_to_file(portfolio):
    choice = input("Do you want to save the portfolio? (yes/no): ").strip().lower()
    if choice != 'yes':
        return
    file_type = input("Save as .txt or .csv? ").strip().lower()
    if file_type == "txt":
        with open("portfolio.txt", "w") as file:
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                file.write(f"{stock}: {qty} shares x ${price} = ${price * qty}\n")
            file.write(f"Total Investment: ${calculate_total(portfolio)}\n")
        print("✅ Saved to 'portfolio.txt'")
    elif file_type == "csv":
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                writer.writerow([stock, qty, price, price * qty])
            writer.writerow(["Total Investment", "", "", calculate_total(portfolio)])
        print("✅ Saved to 'portfolio.csv'")
    else:
        print("❌ Invalid file type. Not saved.")

def main():
    print("📈 Welcome to the Stock Portfolio Tracker!")
    print(f"Available Stocks: {', '.join(STOCK_PRICES.keys())}")
    portfolio = get_user_portfolio()
    if portfolio:
        display_portfolio(portfolio)
        save_to_file(portfolio)
    else:
        print("No portfolio data entered.")

if __name__ == "__main__":
    main()
