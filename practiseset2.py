class DivisionByZeroError(Exception):
    """Custom exception for division by zero errors."""
    def __init__(self, message="Division by zero is not allowed"):
        self.message = message
        super().__init__(self.message)

class Calculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b
    
    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b
    
    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b
    
    def divide(self, a, b):
        """Return the division of a by b, handling division by zero."""
        if b == 0:
            raise DivisionByZeroError()
        return a / b

# Example usage
calc = Calculator()

# Test addition
print("Addition:", calc.add(10, 5))

# Test subtraction
print("Subtraction:", calc.subtract(10, 5))

# Test multiplication
print("Multiplication:", calc.multiply(10, 5))

# Test division
try:
    print("Division:", calc.divide(10, 5))
    print("Division by zero:", calc.divide(10, 0))
except DivisionByZeroError as e:
    print(e)
