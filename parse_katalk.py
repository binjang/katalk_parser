import pandas as pd
import re
import glob
from Checker import check
from Parser import parse

r"""
    input: dir_path (카카오톡 export된 폴더 경로)
    output: DataFrame 또는 list(DataFrame) (concat_everything=False일시)
"""
class KatalkParser(object):
    def __init__(self, dir_path, concat_everything=True):
        self.dir_path = dir_path
        self.concat_everything = concat_everything
        is_folder = (dir_path.find(".") == -1)
        if not is_folder:
            extension = dir_path.split(".")[-1]
        self.is_folder = is_folder
        self.extension = extension

    def parse(self):
        if self.is_folder:
            self.parse_folder(self.dir_path)
        else:
            self.parse_file(self.dir_path)

    def _parse_folder(self):
        dir_path = self.dir_path
        files_list = glob.glob(f"{dir_path}/**/*.txt", recursive=True)
        for filepath in files_list:
            self.parse_file(filepath)

    def _parse_file(self, filepath: str):
        dir_path = filepath
        extension = self.extension
        filetype = self.check_filetype(filepath)
        if filetype == "windows":
            _parse_windows(filepath)
        elif filetype == "mac":
            _parse_mac(filepath)
        elif filetype == "ios":
            _parse_ios(filepath)
        else:
            raise ValueError(f"Unexpected filetype. Please check file: {filepath}")

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

    r"""
        윈도우 줄패턴: \[.+\] \[(오전|오후) \d{1,2}:\d{2}] .+
        
        --------------- n년 n월 n일 n요일 ---------------
        [이름] [오전 n시] 내용
    """
    def _parse_windows(self, filepath):
        with open(filepath, 'r', encoding="utf-8") as f:
            data = f.readlines()
        df = pd.DataFrame(data)
        first_line = df[0][0]
        while first_line[0] != "[":
            df = df[1:].reset_index(drop=True)


    r"""
        맥 줄패턴: read_csv
        
        년-월-일 시:분:초, "이름", "메세지"
    """
    def _parse_mac(self, filepath):
        df = pd.read_csv(filepath)
        #TODO: strip uneccesary lines
        return df

    r"""
        ios 줄패턴: 
    
    """
    def _parse_ios(self, filepath):
        with open(filepath) as f:
            pass
        return df



