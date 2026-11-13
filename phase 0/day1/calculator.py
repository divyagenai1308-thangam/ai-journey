#Calculator: Ask for two numbers, then print their sum, difference, product and division.

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

total = num1 + num2
difference = num1 - num2
product = num1 * num2
division = 0
if num2==0:
    print("Division: not possible, cannot divide by zero")
else:
    division = num1/num2

print(f"Sum of two number: {total}, Difference: {difference}, Product: {product}, Division: {division}")
