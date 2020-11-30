import pytest
import logging
from PythonFor100Days import calc

def setup_module(module):
    logging.info("setup module")
    print("-------module------")


class Test_cacl():

    A = calc.Calc()
    logging.basicConfig(level=logging.DEBUG)

    @classmethod
    def setup_class(cls):
        logging.info("class method")
        print("------class------")

    def setup_method(self):
        logging.info("setUp method")
        print("-------before method-------")

    def teardown_method(self):
        print("------after of method------")

    def test_above(self):
        print("This is test_above.")
        assert self.A.above(1, 5) == False

    def test_add(self):
        print("This is test_add.")
        assert self.A.add(1, 2) == 3


class Test_calc2:

    A = calc.Calc()
    def test_div(self):
        print("This is test_div.")
        assert self.A.div(2, 1) == 2

    def teardown_method(self):
        logging.info("teardown method")