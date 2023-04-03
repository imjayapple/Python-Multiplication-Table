# Take in a simple parameter, number, for which the table will be created
# Print out a message that includes the given number using a formatted string (f-string)
# Use this formula to create a for-loop that can iterate over a range of numbers

def display_multiplication_table(number):
    print(f"\nMultiplication table for {number}:\n")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# Create the logic for the program
# While loop to prompt the user to input a valid value, try-except block
# If valid, call the display_multi.... function, passing the valid integer 'number' as an argument

def main():
    print("Welcome to the Multiplication Table Generator!")

    while True:
        try:
            number = int(input("\nEnter a number for which you want to generate a multiplication table: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    display_multiplication_table(number)

if __name__ == "__main__":
    main()