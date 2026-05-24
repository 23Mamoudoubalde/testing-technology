"""
Functions module with examples and definitions
"""


def greet(name):
    """
    Definition: Greets a person by name
    
    Args:
        name (str): The name of the person to greet
    
    Returns:
        str: A greeting message
    
    Example:
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"


def add(a, b):
    """
    Definition: Adds two numbers together
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: The sum of a and b
    
    Example:
        >>> add(5, 3)
        8
        >>> add(2.5, 1.5)
        4.0
    """
    return a + b


def is_even(num):
    """
    Definition: Checks if a number is even
    
    Args:
        num (int): The number to check
    
    Returns:
        bool: True if the number is even, False otherwise
    
    Example:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    return num % 2 == 0


def reverse_string(text):
    """
    Definition: Reverses a string
    
    Args:
        text (str): The string to reverse
    
    Returns:
        str: The reversed string
    
    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
    """
    return text[::-1]


def find_max(numbers):
    """
    Definition: Finds the maximum value in a list
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        int or float: The largest number in the list
    
    Example:
        >>> find_max([3, 7, 2, 9, 1])
        9
        >>> find_max([10, 5, 15])
        15
    """
    return max(numbers)


if __name__ == "__main__":
    # Example usage
    print(greet("Bob"))
    print(add(10, 20))
    print(is_even(6))
    print(reverse_string("coding"))
    print(find_max([4, 8, 2, 9, 5]))
