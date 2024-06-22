import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Lee un archivo CSV desde una ruta o URL y muestra las primeras cinco filas
    y la estructura del dataframe.

    Parameters:
        file_path (str): La ruta o URL del archivo CSV.

    Returns:
        pd.DataFrame: El dataframe leído.
    """
    df = pd.read_csv(file_path)
    print("Primeras cinco filas del dataframe:")
    print(df.head())
    print("\nEstructura del dataframe:")
    print(df.info())
    return df


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el dataset eliminando todas sus columnas excepto las columnas
    especificadas.

    Parameters:
        df (pd.DataFrame): El dataframe original.

    Returns:
        pd.DataFrame: El dataframe con solo las columnas especificadas.
    """
    columns_to_keep = ['month', 'state', 'permit', 'handgun', 'long_gun']
    df_cleaned = df[columns_to_keep]
    print("\nColumnas después de limpiar el dataframe:")
    print(df_cleaned.columns.tolist())
    return df_cleaned


def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renombra la columna 'long_gun' a 'longgun' en el dataframe.

    Parameters:
        df (pd.DataFrame): El dataframe original.

    Returns:
        pd.DataFrame: El dataframe con el nombre de la columna cambiado.
    """
    df_renamed = df  # Inicialización de df_renamed
    if 'long_gun' in df.columns:
        df_renamed = df.rename(columns={'long_gun': 'longgun'})
        print("Columna 'long_gun' renombrada a 'longgun'.")
    else:
        print("La columna 'long_gun' no existe en el dataframe.")

    print("\nNombres de todas las columnas en el dataframe:")
    print(df_renamed.columns.tolist())
    return df_renamed


def clean(file_path: str) -> pd.DataFrame:
    """
    Ejecuta el proceso completo de lectura, limpieza y renombrado de columnas.

    Parameters:
        file_path (str): La ruta o URL del archivo CSV.

    Returns:
        pd.DataFrame: El dataframe completamente procesado.
    """
    df = read_csv(file_path)
    clean_csv(df)
    rename_col(df)
    return df
