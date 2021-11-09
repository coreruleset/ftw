from abc import ABC, abstractmethod


class LogChecker(ABC):
    """
    LogChecker is an abstract class that integrations with WAFs MUST implement.
    This class is used by the testrunner to test log lines against an expected
    regex
    """
    def __init__(self):
        self.start = None
        self.end = None

    def set_times(self, start, end):
        self.start = start
        self.end = end

    def mark_start(selfj):
        """
        May be implemented to set up the log checker before
        the request is being sent
        """
        pass

    def mark_end(self):
        """
        May be implemented to tell the log checker that
        the response has been received
        """
        pass

    @abstractmethod
    def get_logs(self):
        """
        MUST be implemented, MUST return an array of strings
        These strings represent distinct log lines that were pulled from an
        outside logfile. The times are used by the testrunner to assist the
        implementers in pulling out the correct lines from the log file
        """
        pass
