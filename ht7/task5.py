import pytest
from pytest import mark

def calculate(a, b, action):
   """
    This function calculates the sum / the subtraction / the multiplication / the division of two entered digits based on the selected operator.
   :param a: int, float
   :param b: int, float
   :param action: str: valid options: "+", "-", "*", "/"
   :return: str
   """
   def add(a, b):
       return a + b
   def sub(a, b):
       return a - b
   def mult(a, b):
       return a * b
   def div(a, b):
       return a / b

   actions = {"+": add, "-": sub, "*": mult, "/": div}

   if action in actions:
        return actions[action](a, b)
   else:
        return "Invalid action is selected. Use one of the following actions: +, -, *, /."


class TestCalculate:
    @mark.smoke
    def test01(self):
        # To check the sum of two positive integers
        assert calculate(2,5,"+") == 7

    @mark.smoke
    def test02(self):
        # To check the subtraction of two positive integers
        assert calculate(2,5,"-") == -3

    @mark.smoke
    def test03(self):
        # To check the multiplication of two positive integers
        assert calculate(2,5,"*") == 10

    @mark.smoke
    def test04(self):
        # To check the division of two positive integers
        assert calculate(2,5,"/") == 0.4

    @mark.smoke
    def test05(self):
        # To check error is shown on attempt to use unsupported action
        assert calculate(2,5,"asd") == "Invalid action is selected. Use one of the following actions: +, -, *, /."

    @mark.critical_path
    def test06(self):
        # To check ZeroDivisionError
        with pytest.raises(ZeroDivisionError):
            assert calculate(2, 0, "/")

    @mark.critical_path
    def test07(self):
        # To check the result of multiplication by 0 is 0
        assert calculate(2, 0, "*") == 0

    @mark.critical_path
    def test08(self):
        # To check the sum of int and float results in float
        assert calculate(2, 2.5, "+") == 4.5

    @mark.critical_path
    def test09(self):
        # To check the sum of two negative numbers is negative
        assert calculate(-2, -2.5, "+") == -4.5

    @mark.critical_path
    def test10(self):
        # To check the addition of a negative number is the same as subtraction
        assert calculate(5, -2.5, "+") == 2.5

    @mark.extended
    def test11(self):
        # To check TypeError
        with pytest.raises(TypeError):
            assert calculate("-2", "-2.5", "/")

    @mark.extended
    def test12(self):
        # To check the division of two negative numbers results in positive number
        assert calculate(-10, -2, "/") == 5.0

    @mark.extended
    def test13(self):
        # To check error is shown when action is not specified
        assert calculate(-10, -2, "") == "Invalid action is selected. Use one of the following actions: +, -, *, /."

    @mark.extended
    def test14(self):
        # To check the correctness of the sum of small and big numbers
        assert calculate(10000000000, 2, "+") == 10000000002.0

    @mark.extended
    def test15(self):
        # To check the correctness of the division a big number
        assert calculate(10000000000, 2, "/") == 5000000000.0