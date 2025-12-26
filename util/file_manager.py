import pandas as pd


class CSVFileManager:
    """
    Clase encargada de la lectura y escritura de archivos CSV.
    Se función es tanto cargar los datos desde un archivo CSV y
    devolverlos en forma de DataFrame como convertir un
    DataFrame en un archivo CSV y guardarlo.
    """

    def __init__(self, path: str):

        # Ruta del archivo CSV
        self.path = path

    def read(self) -> pd.DataFrame:
        """
        Lee el archivo CSV de la ruta y devuelve su
        contenido como un DataFrame de pandas.
        """
        return pd.read_csv(self.path)

    def write(self, dataFrame: pd.DataFrame):

        # Convierte un DataFrame en un archivo CSV.
        dataFrame.to_csv(self.path, index=False)
