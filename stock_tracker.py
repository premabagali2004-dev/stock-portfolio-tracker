# TASK 2: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 190,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\\nAvailable Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

try:
    n = int(input("\\nHow many different stocks do you want to buy? "))

    if n <= 0:
        print("Please enter a number greater than zero.")
    else:
        for _ in range(n):
            stock_name = input("\\nEnter stock name: ").strip().upper()

            if stock_name not in stock_prices:
                print("Stock not available!")
                continue

            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than zero!")
                    continue
            except ValueError:
                print("Please enter a valid whole-number quantity.")
                continue

            investment = stock_prices[stock_name] * quantity
            portfolio[stock_name] = portfolio.get(stock_name, 0) + investment
            total_investment += investment
            print(f"Investment in {stock_name} = ${investment}")

        print("\\n========== YOUR PORTFOLIO ==========")
        for stock, value in portfolio.items():
            print(f"{stock}: ${value}")

        print("------------------------------------")
        print(f"Total Investment = ${total_investment}")

        save = input("\\nDo you want to save the result? (yes/no): ").strip().lower()
        if save == "yes":
            with open("stock_portfolio.txt", "w", encoding="utf-8") as file:
                file.write("STOCK PORTFOLIO TRACKER\\n")
                file.write("=======================\\n")
                for stock, value in portfolio.items():
                    file.write(f"{stock}: ${value}\\n")
                file.write("-----------------------\\n")
                file.write(f"Total Investment: ${total_investment}\\n")
            print("Portfolio saved successfully as stock_portfolio.txt")

        print("\\nThank you for using Stock Portfolio Tracker!")

except ValueError:
    print("Please enter a valid whole number.")
