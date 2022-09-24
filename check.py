class Checker(object):

    def __init__(self):
        self.

    def check_filetype(self, filepath):
        with open(filepath) as f:
            for line in f:
                pass
            sample_line = line #TODO: how to find sample line?

        if self._is_windows(sample_line):
            return "windows"
        elif self._is_mac(sample_line):
            return "mac"
        elif self._is_ios(sample_line):
            return "ios"
        else:
            raise ValueError(f"Unexpected filetype. Please check file: {filepath}")

    def _is_windows(self, sample_line, pattern="\[(공격자|방어자)\] \[\D{2} \d{1,2}\:\d{2}\]"):
        return bool(re.search(pattern, sample_line))

    def _is_mac(self, sample_line, pattern="\d{4}-\d{2}-\d{2} \d{2}\:\d{2}\:\d{2},\"(공격자|방어자)\","):
        return bool(re.search(pattern, sample_line))

    def _is_ios(self, sample_line, pattern=""): #TODO: add ios pattern
        return bool(re.search(pattern, sample_line))