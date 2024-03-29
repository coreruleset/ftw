from ftw import testrunner, http, errors
import pytest


@pytest.mark.skip(
    reason="""
    1. ieee.org has a very bad web server, so responses fail a lot
    2. ieee.org sends multiple set-cookie headers and ftw can only handle a single header of the same name"""
)
def test_default(ruleset, test, destaddr):
    """
    Default tester with no logger obj. Useful for HTML contains and Status code
    Not useful for testing loggers
    """
    runner = testrunner.TestRunner()
    try:
        last_ua = http.HttpUA()
        for stage in test.stages:
            if destaddr is not None:
                stage.input.dest_addr = destaddr
            if stage.input.save_cookie:
                runner.run_stage(stage, http_ua=last_ua)
            else:
                runner.run_stage(stage, logger_obj=None, http_ua=None)
    except errors.TestError as e:
        e.args[1]['meta'] = ruleset.meta
        pytest.fail('Failure! Message -> {0}, Context -> {1}'.format(
                    e.args[0], e.args[1]))
