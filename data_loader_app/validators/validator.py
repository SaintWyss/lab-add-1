import pandas as pd

class Validator:
    def __init__(self, datos):
        self._df = pd.DataFrame(datos)

    def validar(self):
        df = self._df.copy()
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        return df.to_dict(orient='records')