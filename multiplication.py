# Take in a simple parameter, number, for which the table will be created
# Print out a message that includes the given number using a formatted string (f-string)
# Use this formula to create a for-loop that can iterate over a range of numbers

def display_multiplication_table(number):
    print(f"\nMultiplication table for {number}:\n")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")