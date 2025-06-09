# Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.
def total(numbers):
    """
    This function takes a list of integers and returns their total sum.
    
    :param numbers: List of integers
    :return: Total sum of the integers in the list
    """
    a = 0 # Initialize a variable to hold the total sum
    for i in numbers:
        a += i  # Add each integer to the total sum
    return sum(numbers)

# Example usage
numbers = [1, 2, 3, 4, 5]
print(total(numbers))  # Output: 15

# Write a function named count that takes a list of integers as input, and returns the number of integers in that list.
def count(number):
  return len(number)

number = [1, 2, 3, 4, 5]
print(count(numbers))  #
