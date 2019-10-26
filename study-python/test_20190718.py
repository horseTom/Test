
import pytest
order = []
@pytest.mark.usefixtures('mod_setup')


class TestA():
    @pytest.mark.usefixtures('clsA_teardown')
    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert 2 > 1

    def test_3(self):
        assert True != False

    # @pytest.fixture(scope='class')
    # def teardown_class():
    #     print("TestA 数据清理")

class TestB:
    def test_4(func):
        assert 1 == 1

    def test_5(self):
        assert 1 < 2

    @pytest.fixture(params=[(1,1,2),(1,2,3),(1,4,5)])
    # mark.parametrize("a,b,c",)
    def test_6(self,a,b,c):
        assert a+b == c

class TestC:

    def test_7(test_8):
        assert 1 == 1


    def test_8(self):
        assert 1 == 1
        order.append("test_8")


    def test_9(self):
        assert 1 == 1
