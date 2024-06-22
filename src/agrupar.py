import pandas as pd


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los datos por 'year' y 'state' y calcula los valores acumulados.

    Parameters:
        df (pd.DataFrame): Dataframe con las columnas 'year' y 'state'.

    Returns:
        pd.DataFrame: Dataframe agrupado por 'year' y 'state' con valores acumulados.
    """
    grouped_df = df.groupby(['year', 'state']).sum().reset_index()
    print("Dataframe agrupado por 'year' y 'state':")
    print(grouped_df.head())
    return grouped_df


def print_biggest_handguns(df: pd.DataFrame) -> None:
    """
    Imprime el estado y el año con el mayor número de hand_guns.

    Parameters:
        df (pd.DataFrame): El dataframe agrupado por estado y año.

    Outputs:
        None
    """
    max_row = df.loc[df['handgun'].idxmax()]
    print(f"El mayor número de hand_guns se registró en {max_row['state']} "
          f"en el año {max_row['year']} con un total de {max_row['handgun']} hand_guns.")


def print_biggest_longguns(df: pd.DataFrame) -> None:
    """
    Imprime el estado y el año con el mayor número de long_guns.

    Parameters:
        df (pd.DataFrame): El dataframe agrupado por estado y año.

    Outputs:
        None
    """
    max_row = df.loc[df['long_gun'].idxmax()]
    print(f"El mayor número de long_guns se registró en {max_row['state']} "
          f"en el año {max_row['year']} con un total de {max_row['long_gun']} long_guns.")
