from art import logo

print(logo)


def add(num1, num2):
    return num1 + num2


def substract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculation():
    num1 = float(input("Enter first number: "))
    for symbol in operation:
        print(symbol)
    continue_calculation = True
    while continue_calculation:
        selected_operation = input("Pick an operation to perform: ")
        num2 = float(input("Enter next number: "))
        calculation_function = operation[selected_operation]
        result = calculation_function(num1, num2)
        print(f"{num1}  {selected_operation}  {num2} =  {result}")

        option = input(f"Type y to continue calculating with {result} , n to exit , s to start a fresh calculation")
        if option == 'y':
            num1 = result
        elif option == 'n':
            exit()
        else:
            continue_calculation = False
            calculation()


calculation()
