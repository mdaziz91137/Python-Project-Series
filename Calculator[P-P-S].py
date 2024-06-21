# Import the time module to add delays in the program execution
import time

# Taking input from the user for two numbers
num1 = input("Enter the First Number :")
num2 = input("Enter the Second Number :")

# Converting the input strings into floats and handling invalid input
try:
    num1 = float(num1)  # Convert first input to float
    num2 = float(num2)  # Convert second input to float
except:
    # If conversion fails, print an error message and exit the program
    print("Please Enter the Valid Inputs")
    exit()

# Adding a delay of 1 second before showing the menu options
time.sleep(1)

# Displaying the menu options with a slight delay between each option for better user experience
print("1. Addition")
time.sleep(0.2)
print("2. Subtraction")
time.sleep(0.2)
print("3. Multiply")
time.sleep(0.2)
print("4. Divide")
time.sleep(0.2)

# Taking input from the user to select an operation
answer = input("Please Enter the According the above")

# Making conditions to check which operation the user wants to perform
if answer == "1":
    # If user selects 1, perform addition
    ans_add = num1 + num2
    print("Result :", ans_add)
elif answer == "2":
    # If user selects 2, perform subtraction
    ans_sub = num1 - num2
    print("Result :", ans_sub)
elif answer == "3":
    # If user selects 3, perform multiplication
    ans_mul = num1 * num2
    print("Result :", ans_mul)
elif answer == "4":
    # If user selects 4, perform division
    if num2 != 0:
        # Ensure the second number is not zero to avoid division by zero error
        ans_div = num1 / num2
        print("Result :", ans_div)
    else:
        # If second number is zero, print an error message
        print("Error!")
else:
    # If user enters an invalid option, print an error message
    print("Please Enter a Valid Number")
