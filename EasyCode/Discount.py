def calculate_total_price(prices, discount):
    total_price = round((prices - (prices * discount / 100)),2)
    return total_price


def product_discount():
    discount = float(input("Discount on product: "))
    if discount < 0 or discount > 100:
        print("Invalid Discount Value Entered")
        exit()
    quantity = int(input("No of product: "))
    if quantity < 0:
        print("Invalid Quantity Value Entered")
        exit()
    price = []
    prices = 0
    for i in range(quantity):
        price.append(float(input("Price of product: ")))
        if 0 > price[i]:
            print("Invalid Price Inserted")
            exit()
        prices += price[i]
    total_price = calculate_total_price(prices, discount)
    print(f"Total Price to pay: {total_price}")


product_discount()
