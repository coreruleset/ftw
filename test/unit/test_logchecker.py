from ftw import logchecker
import pytest


def test_logchecker_abstract():
    with pytest.raises(TypeError):
        logchecker.LogChecker()


class LogChecker(logchecker.LogChecker):
    def get_logs(self):
        return None


def test_logchecker_impl():
    LogChecker()
