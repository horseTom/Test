import logging
import pytest

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture(scope="module")
def mod_setup():
    logging.info("login")

def mod_teardown():
    logging.info("module数据清理！")

@pytest.fixture(scope='class')
def clsA_teardown():
    logging.info("class A teardown")

@pytest.fixture(scope='function')
def func(self):
    logging.info("TestB 方法初始化")