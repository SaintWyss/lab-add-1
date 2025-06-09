import pandas as pd
from .base_reader import BaseReader

class CSVReader(BaseReader):
    def leer_datos(self):
        df = pd.read_csv(self._path)
        return df.to_dict(orient='records')