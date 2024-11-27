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
    @mark.parametrize('a,b,action,result',[(2, 5, "+", 7),
                                           (2, 5, "-", -3),
                                           (2, 5, "*", 10),
                                           (2, 5, "/", 0.4),
                                           (2, 5, "asd", "Invalid action is selected. Use one of the following actions: +, -, *, /.")])
    def test_smoke(self,a,b,action,result):
        assert calculate(a,b,action) == result

    @mark.critical_path
    @mark.parametrize('a,b,action,result', [(2, 0, "*", 0),
                                            (2, 2.5, "+", 4.5),
                                            (-2, -2.5, "+", -4.5),
                                            (5, -2.5, "+", 2.5)])
    def test_critical_path(self, a, b, action, result):
        assert calculate(a, b, action) == result

    @mark.extended
    @mark.parametrize('a,b,action,result', [(-10, -2, "/", 5.0),
                                            (-10, -2, "", "Invalid action is selected. Use one of the following actions: +, -, *, /."),
                                            (10000000000, 2, "+", 10000000002.0),
                                            (10000000000, 2, "/", 5000000000.0)])
    def test_extended(self, a, b, action, result):
        assert calculate(a, b, action) == result

    @mark.extended
    @mark.parametrize('a,b,action,error', [(2, 0, "/", ZeroDivisionError),
                                           ("-2", "-2.5", "/", TypeError)])
    def test_errors(self,a,b,action,error):
        with pytest.raises(error):
            assert calculate(a, b, action)