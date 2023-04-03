import pandas as pd
from colorama import Fore

class Dataset:
    filepath: str
    sep: str = ","
    header: int = 0
    index_col: int = None
    names: list[str] = None
    encoding: str = "utf-8"
    skip_blank_lines: bool = True
    na_values: str = ""

    dataframe: pd.DataFrame = None

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
        except Exception:
            print(Fore.RED + "[FATAL] File not found.")
            exit(1)

    def __str__(self):
        if self.dataframe:
            return str(self.dataframe.head())
        else:
            return "Empty DataFrame."
 