import sys
import math
from contextlib import redirect_stdout


def calculate_total_price(prices, discount):
    total_price = round(int(prices - (prices * discount / 100)))
    return total_price


def main():
    discount = int(input("Discount on product: "))
    n = int(input("No of product: "))
    if 0 > n > 100:
        exit()
    if 0 >= discount >= 100:
        exit()
    price = []
    prices = 0
    for i in range(n):
        price.append(int(input("Price of product: ")))
        if 0 > price[i] > 100000:
            exit()
        prices += price[i]
    total_price = calculate_total_price(prices, discount)
    print(f"Result is: {total_price}")


if __name__ == '__main__':
    main()
