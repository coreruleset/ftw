from ftw import testrunner


def test_multipart(ruleset, test):
    runner = testrunner.TestRunner()
    for stage in test.stages:
        runner.run_stage(stage)
