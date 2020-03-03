from ftw import testrunner


def test_runner(ruleset, test):
    runner = testrunner.TestRunner()
    for stage in test.stages:
        runner.run_stage(stage)
