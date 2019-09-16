from ftw import logchecker
import pytest


def test_logchecker():
    with pytest.raises(TypeError):
        logchecker.LogChecker()
