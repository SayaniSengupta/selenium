import pytest


@pytest.mark.usefixtures("setup")
class Testexample:

    def test_f(self):
        print("say-ani")

    def test_f1(self):
        print("say-ani1")

    def test_f2(self):
        print("say-ani2")

    def test_f3(self):
        print("say-ani3")
