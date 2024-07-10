# name="jai"
# x=5
# print(name)#
# #iron
# MyVar2="zero"

# print(x)


# Define functions for calculator operations

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Main program to interact with user

def main():
    print("Welcome to Simple Calculator")

    while True:
        try:
            # Input from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")

            # Perform calculation based on operator
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator")
                continue

            print(f"Result: {result}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")

        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            break

    print("Thank you for using Simple Calculator")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

# Backend functions for calculator operations

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Function to handle button click and perform calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = entry_operator.get()

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            raise ValueError("Invalid operator")

        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

label_operator = tk.Label(root, text="Enter operator (+, -, *, /):")
label_operator.pack()
entry_operator = tk.Entry(root)
entry_operator.pack()

# Result field (disabled)
label_result = tk.Label(root, text="Result:")
label_result.pack()
entry_result = tk.Entry(root, state='disabled')
entry_result.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Run the main event loop
root.mainloop()


