
import pytest

@pytest.mark.usefixtures('module')
@pytest.mark.run(order=1)
class TestA:
    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert 2 > 1

    def test_3(self):
        assert True != False

    @classmethod
    def teardown_class(cls):
        print("TestA 数据清理")

@pytest.mark.run(order=2)
class TestB:
    def setup_method(self):
        print("TestB 方法初始化")

    def test_4(self):
        assert 1 == 1

    def test_5(self):
        assert 1 < 2

    @pytest.mark.parametrize("a,b,c", [(1,1,2),(1,2,3),(1,4,5)])
    def test_6(self,a,b,c):
        assert a+b == c

class TestC:
    @pytest.mark.run(order=5)
    def test_7(self):
        assert 1 == 1

    @pytest.mark.run(order=3)
    def test_8(self):
        assert 1 == 1

    @pytest.mark.run(order=4)
    def test_9(self):
        assert 1 == 1

