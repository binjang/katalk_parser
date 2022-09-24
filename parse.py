import pandas as pd
import re

class Parser(object):
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

    r"""
        윈도우 줄패턴: \[.+\] \[(오전|오후) \d{1,2}:\d{2}] .+

        --------------- n년 n월 n일 n요일 ---------------
        [이름] [오전 n시] 내용
        
        시간 | 사용자 | 내용 순으로 파실
    """
    def _parse_windows(self, filepath):
        with open(filepath, 'r', encoding="utf-8") as f:
            data = f.readlines()
        df = pd.DataFrame(data)
        first_line = df[0][0]
        while first_line[0] != "[":
            df = df[1:].reset_index(drop=True)

        if self.include_filepath:
            paths = []
        times, names, messages = [], [], []
        for i, row in df.iterrows():
            matches = re.findall("\[.+?\]", row)
            times.append(matches[1][1, -1])
            names.append(matches[0][1, -1])




        return df

    r"""
        맥 줄패턴: 
        년-월-일 시:분:초, "이름", "메세지"
    """
    def _parse_mac(self, filepath):
        df = pd.read_csv(filepath)

        return df

    r"""
        ios 줄패턴: 
        n년 n월 n일 n요일
        월/일/년 오전 시:분, 이름 : 메세지
    """
    def _parse_ios(self, filepath):
        with open(filepath) as f:
            pass
        return df

    r"""
        안드로이드 줄패턴: 
        n년 n월 n일 오전 시:분
        n년 n월 n일 오전 시:분, 이름 : 메세지 

   """
    def _parse_android(self, filepath):
        with open(filepath) as f:
            pass
        return df

    r"""
        postprocess deleted messages, e.g.
            삭제된 메시지입니다.
            This message was deleted.
    """
    def _postprocess(self):  # TODO: strip unnecessary lines
        pass
