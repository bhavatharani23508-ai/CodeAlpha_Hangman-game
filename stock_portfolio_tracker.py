stocks = {
    "GOOGLE": 180,
    "MICROSOFT": 250,
    "SAMSUNG": 320,
    "CODSOFT": 140
}
total_amount = 0
count = int(input("How many stocks do you want to enter? : "))
for i in range(count):
    name = input("\nEnter stock name : ").upper()
    try:
        quantity = int(input("Enter quantity : "))
    except ValueError:
        print("Please enter numbers only for quantity.")
        continue
    if name in stocks:
        price = stocks[name]
        investment = price * quantity
        total_amount += investment
        print("Investment Value :", investment)
    else:
        print("Stock not available.")
print("\nTotal Investment :", total_amount)
