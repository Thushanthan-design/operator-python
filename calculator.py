# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


def history_method():
    global history
    if not history:
        print('There is no histroy before')
    else:
        for i in history:
            print('fist Number : ', i[0], ' second number : ', i[1], ' operator is : ', i[2], ' answer is ', i[3])


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

history = []

while True:
    history_list = []
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    if choice == 1:
        history_list.append('add operator')
    elif choice == 2:
        history_list.append('sub operator')
    elif choice == 3:
        history_list.append('Multi operator')
    elif choice == 4:
        history_list.append('division operator')

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        history_list.append(num1)
        num2 = float(input("Enter second number: "))
        history_list.append(num2)

        if choice == '1':
            history_list.append('+')
            history_list.append(add(num1, num2))
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            history_list.append('-')
            history_list.append(subtract(num1, num2))
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            history_list.append('*')
            history_list.append(multiply(num1, num2))
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            history_list.append('/')
            history_list.append(divide(num1, num2))
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        # print('history', history_list)
        history.append(history_list)
        # print(history)
        his = input("Do you need to see history? (yes/no): ")
        if his == 'yes':
            history_method()
        else:
            print('ok')

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
