import pytest

class Test_Pytest_Object:

    @pytest.mark.parametrize('num', [3, 4, 2, 1])
    def test_two(self, num):
        x = 5
        assert x > num

    def test_one(self):
        assert False == True