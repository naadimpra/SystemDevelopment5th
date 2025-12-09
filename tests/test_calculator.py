"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # TODO: Implement

        #Arrange
        calc = Calculator()
        a = 10
        b = 3
        expected = 7

        #Act
        result = calc.subtract(a, b)

        #Assert
        assert result == expected

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""

        #Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -2

        #Act
        result = calc.subtract(a, b)

        #Assert
        assert result == expected

    def test_subtract_positive_and_negative(self):
        """Test subtracting negative number from positive number."""

        #Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 8

        #Act
        result = calc.subtract(a, b)

        #Assert
        assert result == expected

    def test_subtract_negative_and_positive(self):
        """Test subtracting positive number from negative number."""

        #Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -8

        #Act
        result = calc.subtract(a, b)

        #Assert
        assert result == expected

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""

        #Arrange
        calc = Calculator()
        a = 7.5
        b = 2.5
        expected = 5.0

        #Act
        result = calc.subtract(a, b)

        #Assert
        assert result == pytest.approx(expected)

    def test_subtract_resulting_in_zero(self):
        """Test subtracting two equal numbers resulting in zero."""

        #Arrange
        calc = Calculator()
        a = 4
        b = 4
        expected = 0

        #Act
        result = calc.subtract(a, b)

        #Assert
        assert result == expected

    def test_subtract_with_zero(self):
        """Test subtracting zero from a number."""

        #Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        #Act
        result = calc.subtract(a, b)

        #Assert
        assert result == expected

    def test_subtract_zero_from_number(self):
        """Test subtracting a number from zero."""

        #Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = -5

        #Act
        result = calc.subtract(a, b)

        #Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # TODO: Implement

        #Arrange
        calc = Calculator()
        a = 4
        b = 5
        expected = 20

        #Act
        result = calc.multiply(a, b)

        #Assert
        assert result == expected

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""

        #Arrange
        calc = Calculator()
        a = -4
        b = -5
        expected = 20

        #Act
        result = calc.multiply(a, b)

        #Assert
        assert result == expected

    def test_multiply_positive_and_negative(self):
        """Test multiplying positive and negative numbers."""

        #Arrange
        calc = Calculator()
        a = 4
        b = -5
        expected = -20

        #Act
        result = calc.multiply(a, b)

        #Assert
        assert result == expected

    def test_multiply_negative_and_positive(self):
        """Test multiplying negative and positive numbers."""

        #Arrange
        calc = Calculator()
        a = -4
        b = 5
        expected = -20

        #Act
        result = calc.multiply(a, b)

        #Assert
        assert result == expected

    def test_multiply_with_zero(self):
        """Test multiplying a number with zero."""

        #Arrange
        calc = Calculator()
        a = 7
        b = 0
        expected = 0

        #Act
        result = calc.multiply(a, b)

        #Assert
        assert result == expected

    def test_multiply_zero_with_number(self):
        """Test multiplying zero with a number."""

        #Arrange
        calc = Calculator()
        a = 0
        b = 7
        expected = 0

        #Act
        result = calc.multiply(a, b)

        #Assert
        assert result == expected

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""

        #Arrange
        calc = Calculator()
        a = 2.5
        b = 4.0
        expected = 10.0

        #Act
        result = calc.multiply(a, b)

        #Assert
        assert result == pytest.approx(expected)

    def test_multiply_by_one(self):
        """Test multiplying a number by one."""

        #Arrange
        calc = Calculator()
        a = 9
        b = 1
        expected = 9

        #Act
        result = calc.multiply(a, b)

        #Assert
        assert result == expected

    def test_multiply_one_by_number(self):
        """Test multiplying one by a number."""

        #Arrange
        calc = Calculator()
        a = 1
        b = 9
        expected = 9

        #Act
        result = calc.multiply(a, b)

        #Assert
        assert result == expected

class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # TODO: Implement

        #Arrange
        calc = Calculator()
        a = 10
        b = 2
        expected = 5

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == expected

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 0

        # Act
        with pytest.raises(ValueError) as excinfo:
            calc.divide(a, b)

        # Assert
        assert "Cannot divide by zero" in str(excinfo.value)

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""

        #Arrange
        calc = Calculator()
        a = -10
        b = -2
        expected = 5

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == expected

    def test_divide_positive_by_negative(self):
        """Test dividing positive number by negative number."""

        #Arrange
        calc = Calculator()
        a = 10
        b = -2
        expected = -5

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == expected

    def test_divide_negative_by_positive(self):
        """Test dividing negative number by positive number."""

        #Arrange
        calc = Calculator()
        a = -10
        b = 2
        expected = -5

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == expected

    def test_divide_floats(self):
        """Test dividing floating point numbers."""

        #Arrange
        calc = Calculator()
        a = 7.5
        b = 2.5
        expected = 3.0

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == pytest.approx(expected)

    def test_divide_resulting_in_fraction(self):
        """Test dividing numbers resulting in a fraction."""

        #Arrange
        calc = Calculator()
        a = 1
        b = 4
        expected = 0.25

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == pytest.approx(expected)

    def test_divide_by_one(self):
        """Test dividing a number by one."""

        #Arrange
        calc = Calculator()
        a = 9
        b = 1
        expected = 9

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == expected

    def test_divide_one_by_number(self):
        """Test dividing one by a number."""

        #Arrange
        calc = Calculator()
        a = 1
        b = 4
        expected = 0.25

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == pytest.approx(expected)

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""

        #Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 0

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == expected

    def test_divide_number_by_itself(self):
        """Test dividing a number by itself."""

        #Arrange
        calc = Calculator()
        a = 7
        b = 7
        expected = 1

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == expected

    def test_divide_floats_resulting_in_long_decimal(self):
        """Test dividing floats resulting in long decimal."""

        #Arrange
        calc = Calculator()
        a = 1.0
        b = 3.0
        expected = 0.3333333

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == pytest.approx(expected, rel=1e-6)

    def test_divide_negative_floats(self):
        """Test dividing negative floating point numbers."""

        #Arrange
        calc = Calculator()
        a = -7.5
        b = -2.5
        expected = 3.0

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == pytest.approx(expected)

    def test_divide_positive_by_negative_float(self):
        """Test dividing positive float by negative float."""

        #Arrange
        calc = Calculator()
        a = 7.5
        b = -2.5
        expected = -3.0

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == pytest.approx(expected)

    def test_divide_negative_by_positive_float(self):
        """Test dividing negative float by positive float."""

        #Arrange
        calc = Calculator()
        a = -7.5
        b = 2.5
        expected = -3.0

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == pytest.approx(expected)

    def test_divide_small_numbers(self):
        """Test dividing very small numbers."""

        #Arrange
        calc = Calculator()
        a = 0.0001
        b = 0.00001
        expected = 10.0

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == pytest.approx(expected)

    def test_divide_by_negative_one(self):
        """Test dividing a number by negative one."""

        #Arrange
        calc = Calculator()
        a = 9
        b = -1
        expected = -9

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == expected

    def test_divide_negative_one_by_number(self):
        """Test dividing negative one by a number."""

        #Arrange
        calc = Calculator()
        a = -1
        b = 4
        expected = -0.25

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == pytest.approx(expected)

    def test_divide_by_itself_negative(self):
        """Test dividing a negative number by itself."""

        #Arrange
        calc = Calculator()
        a = -8
        b = -8
        expected = 1

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == expected

    def test_divide_by_itself_positive(self):
        """Test dividing a positive number by itself."""

        #Arrange
        calc = Calculator()
        a = 8
        b = 8
        expected = 1

        #Act
        result = calc.divide(a, b)

        #Assert
        assert result == expected

    def test_divide_by_zero_raises_value_error_with_message(self):
        """Test division by zero raises ValueError and checks the exact message."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 0

        # Act
        with pytest.raises(ValueError) as excinfo:
            calc.divide(a, b)

        # Assert
        assert str(excinfo.value) == "Cannot divide by zero"

class TestPower:
    """Tests for the power method."""

    def test_power_positive_exponent(self):
        """Test raising a number to a positive exponent."""
        # Arrange
        calc = Calculator()
        base = 2
        exponent = 3
        expected = 8

        # Act
        result = calc.power(base, exponent)

        # Assert
        assert result == expected

    def test_power_zero_exponent(self):
        """Test raising a number to the zero exponent."""
        # Arrange
        calc = Calculator()
        base = 5
        exponent = 0
        expected = 1

        # Act
        result = calc.power(base, exponent)

        # Assert
        assert result == expected

    def test_power_negative_base_positive_exponent(self):
        """Test raising a negative base to a positive exponent."""
        # Arrange
        calc = Calculator()
        base = -2
        exponent = 3
        expected = -8

        # Act
        result = calc.power(base, exponent)

        # Assert
        assert result == expected

class TestSquareRoot:
    """Tests for the square_root method."""

    def test_square_root_perfect_square(self):
        """Test square root of a perfect square."""
        # Arrange
        calc = Calculator()
        value = 16
        expected = 4

        # Act
        result = calc.sqrt(value)

        # Assert
        assert result == expected

    def test_square_root_non_perfect_square(self):
        """Test square root of a non-perfect square."""
        # Arrange
        calc = Calculator()
        value = 20
        expected = 4.47213595499958  # Approximate value

        # Act
        result = calc.sqrt(value)

        # Assert
        assert result == pytest.approx(expected)

    def test_square_root_of_zero(self):
        """Test square root of zero."""
        # Arrange
        calc = Calculator()
        value = 0
        expected = 0.0

        # Act
        result = calc.sqrt(value)

        # Assert
        assert result == expected

    def test_square_root_of_negative_raises_value_error(self):
        """Test square root of a negative number raises ValueError."""
        # Arrange
        calc = Calculator()
        value = -1

        # Act
        with pytest.raises(ValueError) as excinfo:
            calc.sqrt(value)

        # Assert
        assert "Cannot calculate square root of a negative number" in str(excinfo.value)

    def test_square_root_of_zero(self):
        """Test square root of zero."""
        # Arrange
        calc = Calculator()
        value = 0
        expected = 0.0

        # Act
        result = calc.sqrt(value)

        # Assert
        assert result == expected

class TestModulo:
    """Tests for the modulo method."""

    def test_modulo_positive_numbers(self):
        """Test modulo of positive numbers."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 3
        expected = 1

        # Act
        result = calc.modulo(a, b)

        # Assert
        assert result == expected

    def test_modulo_negative_numbers(self):
        """Test modulo of negative numbers."""
        # Arrange
        calc = Calculator()
        a = -10
        b = -3
        expected = -1

        # Act
        result = calc.modulo(a, b)

        # Assert
        assert result == expected

    def test_modulo_positive_dividend_negative_divisor(self):
        """Test modulo of positive dividend by negative divisor."""
        # Arrange
        calc = Calculator()
        a = 10
        b = -3
        expected = -2  # Python's behavior: 10 = (-3)*(-4) + (-2) --> -2
        
        # Act
        result = calc.modulo(a, b)

        # Assert
        assert result == expected

    def test_modulo_negative_dividend_positive_divisor(self):
        """Test modulo of negative dividend by positive divisor."""
        # Arrange
        calc = Calculator()
        a = -10
        b = 3
        expected = 2  # Python's behavior: -10 = 3*(-4) + 2 --> 2
        
        # Act
        result = calc.modulo(a, b)

        # Assert
        assert result == expected

    def test_modulo_by_zero_raises_value_error(self):
        """Test modulo by zero raises ValueError."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 0

        # Act
        with pytest.raises(ValueError) as excinfo:
            calc.modulo(a, b)

        # Assert
        assert "Cannot perform modulo by zero" in str(excinfo.value)

    def test_modulo_by_zero_raises_value_error_with_message(self):
        """Test modulo by zero raises ValueError and checks the exact message."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 0

        # Act
        with pytest.raises(ValueError) as excinfo:
            calc.modulo(a, b)

        # Assert
        assert str(excinfo.value) == "Cannot perform modulo by zero"

class TestInvalidInputHandling:
    """Tests for range validation exceptions (InvalidInputException)."""

    # Setup constants for test boundaries
    MAX_VALID = InvalidInputException.MAX_VALUE
    MIN_VALID = InvalidInputException.MIN_VALUE
    TOO_HIGH = MAX_VALID + 1
    TOO_LOW = MIN_VALID - 1

    def test_add_raises_on_max_exceeded(self):
        """Test that add raises InvalidInputException when the first input is too high."""

        # Arrange
        calc = Calculator()

        # Act
        with pytest.raises(InvalidInputException) as excinfo:
            calc.add(self.TOO_HIGH, 1)

        # Assert
        assert f"Input value {self.TOO_HIGH} is out of allowed range" in str(excinfo.value)

    def test_subtract_raises_on_min_exceeded(self):
        """Test that subtract raises InvalidInputException when the first input is too low."""
        # Arrange
        calc = Calculator()

        # Act
        with pytest.raises(InvalidInputException) as excinfo:
            calc.subtract(self.TOO_LOW, 1)

        # Assert
        assert f"Input value {self.TOO_LOW} is out of allowed range" in str(excinfo.value)

    def test_multiply_raises_on_second_arg_too_high(self):
        """Test that multiply raises InvalidInputException when the second input is too high."""
        # Arrange
        calc = Calculator()

        # Act
        with pytest.raises(InvalidInputException) as excinfo:
            calc.multiply(2, self.TOO_HIGH)

        # Assert
        assert f"Input value {self.TOO_HIGH} is out of allowed range" in str(excinfo.value)

    def test_divide_raises_on_second_arg_too_low(self):
        """Test that divide raises InvalidInputException when the denominator is too low."""
        # Arrange
        calc = Calculator()

        # Act
        with pytest.raises(InvalidInputException) as excinfo:
            calc.divide(10, self.TOO_LOW)

        # Assert
        assert f"Input value {self.TOO_LOW} is out of allowed range" in str(excinfo.value)

    def test_add_at_valid_boundary(self):
        """Test that add works fine with inputs exactly at the MAX_VALUE boundary."""
        # Arrange
        calc = Calculator()
        a = self.MAX_VALID
        b = 0
        expected = self.MAX_VALID

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_subtract_at_invalid_boundary_check(self):
        """Test that subtract raises InvalidInputException if a single input is just under MIN_VALUE."""
        # Arrange
        calc = Calculator()

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(10, self.TOO_LOW)

    def test_subtract_at_valid_boundary(self):
        """Test that subtract works fine with inputs exactly at the MIN_VALUE boundary."""
        # Arrange
        calc = Calculator()
        a = self.MIN_VALID
        b = 0
        expected = self.MIN_VALID

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected