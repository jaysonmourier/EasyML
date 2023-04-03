import pandas as pd
from colorama import Fore

from sklearn.model_selection import train_test_split

class Dataset:
    filepath: str
    sep: str
    header: int = 0
    index_col: int = None
    names: list[str] = None
    encoding: str = "utf-8"
    skip_blank_lines: bool = True
    na_values: str = ""

    dataframe: pd.DataFrame = None
    
    Xtrain: pd.DataFrame = None
    Xtest: pd.DataFrame = None
    Ytrain: pd.DataFrame = None
    Ytest: pd.DataFrame = None

    def __init__(
            self, 
            filepath: str,
            sep: str = ",",
            header: str = 0,
            index_col: int = None,
            names: list[str] = None,
            encoding: str = "utf-8",
            na_values: str = ""
            ):
        self.filepath = filepath
        self.sep = sep
        self.header = header
        self.index_col = index_col
        self.names = names
        self.encoding = encoding
        self.na_values = na_values

    def load(self):
        try:
            self.dataframe = pd.read_csv(
                self.filepath,
                sep=self.sep,
                header=self.header,
                index_col=self.index_col,
                names=self.names,
                encoding=self.encoding,
                skip_blank_lines=self.skip_blank_lines,
                na_values=self.na_values,
            )
        except Exception as e:
            print(Fore.RED + "[FATAL] File not found.")
            print(e)
            exit(1)

    def __str__(self):
        if self.dataframe:
            return str(self.dataframe.head())
        else:
            return "Empty DataFrame."
 