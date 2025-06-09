import pandas as pd
from .base_reader import BaseReader

class JSONReader(BaseReader):
    def leer_datos(self):
        df = pd.read_json(self._path)
        return df.to_dict(orient='records')