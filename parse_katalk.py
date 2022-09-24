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
    def __init__(self, dir_path, concat_everything=True, include_filepath=False):
        self.dir_path = dir_path
        self.concat_everything = concat_everything
        self.include_filepath = include_filepath
        is_folder = (dir_path.find(".") == -1)
        if not is_folder:
            extension = dir_path.split(".")[-1]
        self.is_folder = is_folder
        self.extension = extension







