'''Sample file 1 to test and practice pylint in python'''
# Define a function named 'add' that takes two arguments.
# Argument named 'number1' and 'number2'.
def add(number1, number2):
    '''Function to add number1 and number2'''
    # The function returns the sum of 'number1' and 'number2'.
    return number1 + number2

# Initialize the variable 'NUM1' with the value 4.
NUM1 = 4

# Initialize the variable 'NUM2' with the value 5.
NUM2 = 5

# Call the 'add' function with 'NUM1' and 'NUM2' as arguments and store the result in 'TOTAL'.
TOTAL = add(NUM1, NUM2)

# Print the result of adding 'NUM1' and 'NUM2'.
# Use the 'format' method to insert the values into the string.
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
