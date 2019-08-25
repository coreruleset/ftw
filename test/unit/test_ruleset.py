from ftw import ruleset, errors
import pytest


def test_output():
    with pytest.raises(errors.TestError) as excinfo:
        ruleset.Output({})
    assert(excinfo.value.args[0].startswith('Need at least'))
    with pytest.raises(errors.TestError) as excinfo:
        ruleset.Output({'status': 'derp'})
    assert(excinfo.value.args[0].startswith('Need at least'))
    with pytest.raises(TypeError) as excinfo:
        ruleset.Output({'log_contains': 10})
    ruleset.Output({'status': 200})
    ruleset.Output({'status': [100, 200]})
    with pytest.raises(errors.TestError) as excinfo:
        ruleset.Output({'status': [100, 'derp']})
    assert(excinfo.value.args[0].startswith('Non integers found'))


def test_input():
    input_1 = ruleset.Input()
    assert(input_1.uri == '/')
    headers = {'Host': 'domain.com', 'User-Agent': 'Zack'}
    dictionary = {}
    dictionary['headers'] = headers
    input_2 = ruleset.Input(**dictionary)
    assert(len(input_2.headers.keys()) == 2)
    dictionary_2 = {'random_key': 'bar'}
    with pytest.raises(TypeError):
        ruleset.Input(**dictionary_2)


def test_testobj():
    with pytest.raises(KeyError) as excinfo:
        ruleset.Test({}, {})
    assert 'test_title' in str(excinfo.value)
    stages_dict = {'test_title': 1, 'stages': [{'stage':
                   {'output': {'log_contains': 'foo'}, 'input': {}}}]}
    ruleset.Test(stages_dict, {})


def test_ruleset():
    with pytest.raises(KeyError):
        ruleset.Ruleset({})
