"""
A simple calculator module with basic arithmetic operations.
"""


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    MAX_VALUE = 1000000
    MIN_VALUE = -1000000
pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    def _validate_input(self, *values):
        for value in values:
            if value > InvalidInputException.MAX_VALUE or value < InvalidInputException.MIN_VALUE:
                raise InvalidInputException(
                    f"Input value {value} is out of allowed range."
                    f"[{InvalidInputException.MIN_VALUE}, {InvalidInputException.MAX_VALUE}]"
                )

    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        self._validate_input(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Raise a to the power of b.

        Args:
            a: Base number
            b: Exponent

        Returns:
            Result of a raised to the power of b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate_input(a, b)
        return a ** b
    
    def modulo(self, a, b):
        """Calculate a modulo b.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            Remainder of a divided by b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        self._validate_input(a, b)
        if b == 0:
            raise ValueError("Cannot perform modulo by zero")
        return a % b
    
    def sqrt(self, a):
        """Calculate the square root of a number.

        Args:
            a: The number to find the square root of

        Returns:
            Square root of a

        Raises:
            InvalidInputException: If input is outside valid range
            ValueError: If a is negative
        """
        self._validate_input(a)
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return a ** 0.5 