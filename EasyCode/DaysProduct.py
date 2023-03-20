data = input()
day = int(data[0])
product = int(data[1])

price = []

for d in range(day):
    a = []
    for p in range(product):
        a.append(int(input()))
    price.append(a)

for d in range(day):
    for p in range(product):
        print(price[d][p], end=" ")
    print()

for d in range(day):
    max1 = 0
    for p in range(product):
        if price[d][p] > max1:
            max1 = price[d][p]
    print()
    print(max1, end=" ")
