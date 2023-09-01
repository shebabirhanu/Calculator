def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

#check for undefined
def divide(x, y):
    if y == 0:
        return "Undefined: cannot divide by 0"
    return x / y

print("Select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        break 
    else:
        print("Invalid choice.")
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2) 
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    print("Invalid entry")

print("Result: {.2f}".format(result))