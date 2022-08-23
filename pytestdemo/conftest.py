import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will e executing first")
    yield
    print("last")


@pytest.fixture(scope="class")
def dataload():
    return ["sayani","sengupta"]


@pytest.fixture(params=[("chrome","firefox","IE"),("a","m","v")])
def crossrowser(request):
    return request.param
