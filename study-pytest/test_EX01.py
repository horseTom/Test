import logging
import pytest


@pytest.mark.skip
class TestPytestObject:
    logging.basicConfig(level=logging.DEBUG)

    @classmethod
    def setup_class(cls):
        logging.info("setup_class")

    # def setup_method(self):
    #     logging("setup_method")

    def setup(self):
        logging.info("setup")

    def test_one(self):
        print("test one")
        assert 1 == 1

    def test_two(self):
        assert 't' in 'the'

    def teardown(self):
        logging.info("teardown")

    # def teardown_method(self):
    #     logging("teardown_method")

    @classmethod
    def teardown_class(cls):
        logging.info("teardown_class")