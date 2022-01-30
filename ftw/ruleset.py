import re
from urllib.parse import parse_qsl, unquote, urlencode

from . import errors
from . import util


class Output(object):
    """
    This class holds the expected output from a corresponding FTW HTTP Input
    We are stricter in this definition by requiring at least one of status,
    response_contains, no_log_contains, expect_error, or log_contains
    """
    def __init__(self, output_dict):
        self.STATUS = 'status'
        self.LOG = 'log_contains'
        self.NOTLOG = 'no_log_contains'
        self.RESPONSE = 'response_contains'
        self.ERROR = 'expect_error'
        if output_dict is None:
            raise errors.TestError(
                'No output dictionary found',
                {
                    'function': 'ruleset.Output.__init__'
                }
            )
        self.output_dict = output_dict
        skip_checks = False
        if self.STATUS not in self.output_dict:
            skip_checks = True
        if skip_checks is False and isinstance(output_dict[self.STATUS], list):
            # Check the number of integers in the list
            num_ele = len([s for s in output_dict[self.STATUS]
                           if type(s) is int])
            # If all elements are integers, we're good
            if len(output_dict[self.STATUS]) == num_ele:
                self.status = output_dict[self.STATUS]
            else:
                raise errors.TestError(
                    'Non integers found in Status list',
                    {
                        'status': output_dict[self.STATUS],
                        'function': 'ruleset.Output.__init__'
                    }
                )
        elif skip_checks is False and isinstance(output_dict[self.STATUS],
                                                 int):
            self.status = int(output_dict[self.STATUS])
        else:
            self.status = None
        self.response_contains_str = self.process_regex(self.RESPONSE)
        self.no_log_contains_str = self.process_regex(self.NOTLOG)
        self.log_contains_str = self.process_regex(self.LOG)
        self.expect_error = bool(self.output_dict[self.ERROR]) if \
            self.ERROR in self.output_dict and \
            self.output_dict[self.ERROR] else None
        if self.status is None and self.response_contains_str is None \
                and self.log_contains_str is None \
                and self.no_log_contains_str is None \
                and self.expect_error is None:
            raise errors.TestError(
                'Need at least one status, response_contains '
                ', no_log_contains, or log_contains',
                {
                    'status': self.status,
                    'response_contains value': self.response_contains_str,
                    'log_contains value': self.log_contains_str,
                    'no_log_contains value': self.no_log_contains_str,
                    'expect_error value': self.expect_error,
                    'function': 'ruleset.Output.__init__'
                })

    def process_regex(self, key):
        """
        Extract the value of key from dictionary if available
        and process it as a python regex
        """
        return re.compile(self.output_dict[key]) if \
            key in self.output_dict else None


class Input(object):
    """
    This class holds the data associated with an HTTP Input request in FTW
    """
    def __init__(self, raw_request=None,
                 encoded_request=None,
                 protocol='http',
                 dest_addr='localhost',
                 port=80,
                 method='GET',
                 uri='/',
                 version='HTTP/1.1',
                 headers={},
                 data='',
                 save_cookie=False,
                 stop_magic=False
                 ):
        self.raw_request = raw_request
        self.encoded_request = encoded_request
        self.protocol = protocol
        self.dest_addr = dest_addr
        self.port = port
        self.method = method
        self.uri = uri
        self.version = version
        self.headers = headers
        self.data = data
        # Support data in list format and join on CRLF
        if isinstance(self.data, list):
            self.data = '\r\n'.join(self.data)
        self.save_cookie = save_cookie
        self.stop_magic = stop_magic
        # Check if there is any data and do defaults
        if self.data != '':
            # Default values for content length and header
            if 'Content-Type' not in list(headers.keys()) and \
               stop_magic is False:
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
            # check if encoded and encode if it should be
            if 'Content-Type' in list(headers.keys()):
                if headers['Content-Type'] == \
                   'application/x-www-form-urlencoded' and stop_magic is False:
                    if util.ensure_str(unquote(self.data)) == self.data:
                        query_string = parse_qsl(self.data)
                        if len(query_string) != 0:
                            encoded_args = urlencode(query_string)
                            self.data = encoded_args
            if 'Content-Length' not in list(headers.keys()) and \
               stop_magic is False:
                # The two is for the trailing CRLF and the one after
                headers['Content-Length'] = len(self.data)


class Stage(object):
    """
    This class holds information about 1 stage in a test, which contains
    1 input and 1 output
    """
    def __init__(self, stage_dict, stage_index, test):
        self.stage_dict = stage_dict
        self.stage_index = stage_index
        self.test = test
        self.input = Input(**stage_dict['input'])
        self.output = Output(stage_dict['output'])
        self.id = self.build_id()

    def build_id(self):
        rule_name = self.test.ruleset_meta["name"].split('.')[0]
        return f'{rule_name}-{self.test.test_index}-{self.stage_index}'


class Test(object):
    """
    This class holds information for 1 test and potentially many stages
    """
    def __init__(self, test_dict, test_index, ruleset_meta):
        self.test_dict = test_dict
        self.test_index = test_index
        self.ruleset_meta = ruleset_meta
        self.test_title = self.test_dict['test_title']
        self.stages = self.build_stages()
        self.enabled = True
        if 'enabled' in self.test_dict:
            self.enabled = self.test_dict['enabled']

    def build_stages(self):
        """
        Processes and loads an array of stages from the test dictionary
        """
        return [Stage(stage_dict['stage'], index, self)
                for index, stage_dict in enumerate(self.test_dict['stages'])]


class Ruleset(object):
    """
    This class holds test and stage information from a YAML test file
    These YAML files are used to test the OWASP/Modsec CRSv3 rules
    """
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file
        self.meta = yaml_file['meta']
        self.author = self.meta['author']
        self.description = self.meta['description']
        self.enabled = self.meta['enabled']
        self.tests = self.extract_tests() if self.enabled else []

    def extract_tests(self):
        """
        Processes a loaded YAML document and
        creates test objects based on input
        """
        try:
            return [Test(test_dict, index, self.meta)
                    for index, test_dict in enumerate(self.yaml_file['tests'])]
        except errors.TestError as e:
            e.args[1]['meta'] = self.meta
            raise e
        except Exception as e:
            raise Exception(
                'Caught error. Message: %s on test with metadata: %s'
                % (str(e), str(self.meta))
            )
