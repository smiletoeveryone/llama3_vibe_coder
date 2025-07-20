# Warning: Code might not be valid Python
Here's a simple calculator program in Python:

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x / y

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation.lower() != "yes":
            break
    
    else:
        print("Invalid Input")
```

In this program, we have four functions for basic arithmetic operations: addition, subtraction, multiplication, and division. We then use a while loop to repeatedly ask the user for their choice of operation, take two numbers as input, perform the chosen operation on those numbers, and display the result. The user is also given the option to do another calculation after each operation.