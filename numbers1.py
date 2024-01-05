# Ask the user to enter three different integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Perform calculations
sum = num1 + num2 + num3
first_minus_second = num1 - num2
third_times_first = num3 * num1
sum_divided_by_third = sum/ num3

# Print the results
print("Sum of all numbers:", sum)
print("First number minus second number:", first_minus_second)
print("Third number multiplied by first number:", third_times_first)
print("Sum of all three numbers divided by the third number:", sum_divided_by_third)