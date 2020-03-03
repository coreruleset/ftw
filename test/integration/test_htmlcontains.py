from ftw import ruleset, testrunner, http, errors
import pytest
import re


def test_search_before_response():
    runner = testrunner.TestRunner()
    ruleset.Input(dest_addr="example.com",
                  headers={"Host": "example.com"})
    http_ua = http.HttpUA()
    with pytest.raises(errors.TestError):
        runner.test_response(http_ua.response_object, re.compile('dog'))


def test_search_not_found():
    runner = testrunner.TestRunner()
    x = ruleset.Input(dest_addr="example.com",
                      headers={"Host": "example.com"})
    http_ua = http.HttpUA()
    http_ua.send_request(x)
    with pytest.raises(AssertionError):
        runner.test_response(http_ua.response_object, re.compile('dog'))


def test_search_success():
    runner = testrunner.TestRunner()
    x = ruleset.Input(dest_addr="example.com",
                      headers={"Host": "example.com"})
    http_ua = http.HttpUA()
    http_ua.send_request(x)
    runner.test_response(http_ua.response_object,
                         re.compile('is for use in illustrative'))
