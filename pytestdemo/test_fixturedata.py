import logging

import pytest

from pytestdemo.Baseclass import Baseclass


@pytest.mark.usefixtures("dataload")
class TestFunction(Baseclass):
    def test_edit(self, dataload):
        log = self.getlogger()
        log.info(dataload)


def test_demo2(crossrowser):
    print(crossrowser)


