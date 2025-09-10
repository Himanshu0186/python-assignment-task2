# # Task 1: Read a File and Handle Errors

# try:
#     # Try to open the file in read mode
#     with open("sample.txt", "r") as file:
#         print("Contents of sample.txt:\n")
#         # Print line by line
#         for line in file:
#             print(line.strip())   # strip() removes extra spaces/newlines
# except FileNotFoundError:
#     # If file is missing
#     print("Error: The file 'sample.txt' was not found.")
# except Exception as e:
#     # Any other unexpected error
#     print("An error occurred:", e)





# Task 2: Factorial using Function (Recursion)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}")
except ValueError:
    print("Error: Please enter a valid integer.")
