# Menu-driven calculator for basic arithmetic operations

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract the second number from the first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers with division-by-zero handling
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

# Keep showing the calculator menu until the user chooses Exit
while True:
    print("\n===== MENU-DRIVEN CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Exit the calculator when the user selects option 5
    if choice == "5":
        print("Calculator closed.")
        break

    # Validate the menu choice before asking for numbers
    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please select 1-5.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    # Call the appropriate function based on the selected operation
    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
