import pandas as pd
from . import log
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
    features: list[str] = None
    target: str = None

    dataframe: pd.DataFrame = None
    
    features: list = None
    transformed: dict = None
    target: str = None
    test_size: float

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
        self.dataframe = pd.read_csv(
            filepath,
            #sep,
            #header,
            #index_col,
            #names,
            #encoding,
            #na_values
        )

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
            print(e)
            log.fatal(1, "File not found.")
            exit(1)

    def split(self):
        set_of_features = []
        if self.transformed is not None:
            for feature in self.features:
                if feature in list(self.transformed.keys()):
                    set_of_features.extend(self.transformed[feature]["names"])
                else:
                    set_of_features.extend([feature])
        else:
            self.Xtrain, self.Xtest, self.Ytrain, self.Ytest = train_test_split(self.dataframe[self.features], self.dataframe[self.target], test_size=self.test_size)
            return
        
        self.Xtrain, self.Xtest, self.Ytrain, self.Ytest = train_test_split(self.dataframe[set_of_features], self.dataframe[self.target], test_size=self.test_size)

    def __str__(self):
        if self.dataframe:  
            return self.dataframe.head()
        else:
            return "Empty DataFrame."
 