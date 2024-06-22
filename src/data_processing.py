# src/data_processing.py

import pandas as pd


def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Divide la información de la columna 'month' en dos nuevas columnas 'year' y 'month'.

    Parameters:
        df (pd.DataFrame): El dataframe de entrada.

    Returns:
        pd.DataFrame: El dataframe con la información de la fecha dividida en las dos columnas.
    """
    df[['year', 'month']] = df['month'].str.split('-', expand=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)

    print("Primeras cinco filas del dataframe después de dividir 'month' en 'year' y 'month':")
    print(df.head())

    return df


def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina la columna 'month' del dataframe.

    Parameters:
        df (pd.DataFrame): El dataframe de entrada.

    Returns:
        pd.DataFrame: El dataframe sin la columna 'month'.
    """
    if 'month' in df.columns:
        df = df.drop(columns=['month'])

    print("Primeras cinco filas del dataframe después de eliminar 'month':")
    print(df.head())

    print("Columnas actuales del dataframe:")
    print(df.columns.tolist())

    return df
