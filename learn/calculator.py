# Simple Python Calculator

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Performing calculations
sum_result = num1 + num2 + num3
difference = num1 - num2 - num3
product = num1 * num2 * num3
quotient = num1 / num2 / num3 if num2 != 0 and num3 != 0 else "Undefined (cannot divide by zero)"


# Printing results
print("\nResults:")
print(f"Addition: {sum_result}")
print(f"Subtraction: {difference}")
print(f"Multiplication: {product}")
print(f"Division: {quotient}")
