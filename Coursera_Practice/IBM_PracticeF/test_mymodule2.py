# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'add' function from the 'mymodule2' module.
from mymodule2 import add

# Define a test case class for testing the 'add' function.
# A test case is a single unit of testing. It checks a specific aspect of the code's behavior.
class Testadd(unittest.TestCase): 

    # Define the first test method for the 'add' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        # Check when 0 and 0 are given as input the output must be 0.
        # This tests if the function correctly computes the sum of 2 and 4.
        self.assertEqual(add(2, 4), 6) # test when 2 and 4 are given as input the output is 6.

        # Check when 0 and 0 are given as input the output must be 0.
        # This tests if the function correctly computes the sum of 0.
        self.assertEqual(add(0, 0), 0)  # test when 0 and 0 is given as input the output is 0.

        # Check when 2.3 and 3.6 are given as input the output must be 5.9..
        # This tests that the function's output is 5.9, verifying the use of float.
        self.assertEqual(add(2.3, 3.6), 5.9)  # test when 2.3 and 3.6 is given as input the output is 5.9.

        # Check when the strings "Hello" and "World" are given as input the output must be "HelloWorld".
        # This tests that the function's output is a string, verifying the use of string.
        self.assertEqual(add("Hello", "World"), "HelloWorld") # test when "Hello" and "World" are given as input the output is "HelloWorld"

        # Check when 2.3000 and 4.300 are given as input the output must be 6.6.
        # This tests that the function's output works with float with multiple 0.
        self.assertEqual(add(2.3000, 4.300), 6.6) #

        # Check when -2 and -2 are given as input the output must not be 0.
        # This tests that the function's output is not 0, verifying that the sum of -2 should be -4.
        self.assertNotEqual(add(-2, -2), 0) # test when input is -2 and output is not 0.

# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
unittest.main()
