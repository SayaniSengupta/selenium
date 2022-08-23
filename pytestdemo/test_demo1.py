import pytest


@pytest.mark.skip
def test_first(setup):
    msg = "hi"
    assert msg == "hi","not match"



def test_demo_preset(setup):
    msg = "hi"
    assert msg == "hi","not match"


def test_demo_second(setup):
    msg = "hi"
    assert msg == "hi", "not match"
