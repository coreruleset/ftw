from ftw import testrunner, http, errors
import pytest
import re


def test_response_before_response():
    runner = testrunner.TestRunner()
    http_ua = http.HttpUA()
    with pytest.raises(errors.TestError):
        runner.test_response(http_ua.response_object,
                             re.compile('dog'))


def test_response_failure():
    runner = testrunner.TestRunner()
    http_ua = http.HttpUA()
    with pytest.raises(AssertionError):
        runner.test_response(http.HttpResponse(
                             'HTTP/1.1 200 OK\r\n\r\ncat', http_ua),
                             re.compile('dog'))


def test_response_success():
    runner = testrunner.TestRunner()
    http_ua = http.HttpUA()
    runner.test_response(http.HttpResponse(
                         'HTTP/1.1 200 OK\r\n\r\ncat', http_ua),
                         re.compile('cat'))
