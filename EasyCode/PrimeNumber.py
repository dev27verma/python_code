number = int(input("Enter a number "))

def prime_number(number):
    count = 0
    if number >= 2:
        for num in range(1, number + 1):
            if number % num == 0:
                count += 1
        if count == 2:
            print(f"Number {number} is prime")
        else:
            print(f"Number {number} is not prime")

    else:
        print("invalid number")

prime_number(number)