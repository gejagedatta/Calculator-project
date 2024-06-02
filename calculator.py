def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def division(num1,num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1/num2

print("Select Operation:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter Choice (1/2/3/4): ")

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter First Number:"))
        num2 = float(input("Enter Second Number:"))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-",num2, "=", substract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        break
    else:
        print("Invalid Input")