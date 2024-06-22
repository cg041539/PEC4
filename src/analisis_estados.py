import pandas as pd
from src.data_cleaning import read_csv


def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los valores totales únicamente por estado.

    Parameters:
        df (pd.DataFrame): El dataframe con los datos agrupados por estado y año.

    Returns:
        pd.DataFrame: El dataframe con los valores agrupados únicamente por estados.
    """
    # Agrupar por estado y sumar los valores de todas las demás columnas
    df_state_grouped = df.groupby('state').sum().reset_index()
    if 'year' in df_state_grouped.columns:
        df_state_grouped = df_state_grouped.drop(columns=['year'])
    print("Dataframe agrupado por estado:")
    print(df_state_grouped.head())
    return df_state_grouped


def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina los estados no deseados del dataframe.

    Parameters:
        df (pd.DataFrame): El dataframe con los datos agrupados por estado.

    Returns:
        pd.DataFrame: El dataframe sin los estados no deseados.
    """
    print(f"Número de estados antes de la limpieza: {df['state'].nunique()}")
    states_to_remove = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
    df_cleaned = df[~df['state'].isin(states_to_remove)]
    print(f"Número de estados después de la limpieza: {df_cleaned['state'].nunique()}")
    return df_cleaned


def merge_datasets(df: pd.DataFrame, population_file: str) -> pd.DataFrame:
    """
    Fusiona el conjunto de datos con los datos poblacionales.

    Parameters:
        df (pd.DataFrame): Dataframe con los datos agrupados por estado.
        population_file (str): La ruta del archivo CSV con datos poblacionales.

    Returns:
        pd.DataFrame: Dataframe resultante al fusionar los datos.
    """
    # Leer el archivo de población usando read_csv
    population_df = read_csv(population_file)

    # Fusionar los dataframes
    merged_df = pd.merge(df, population_df, left_on='state', right_on='state')

    # Imprimir las primeras cinco filas del dataframe resultante
    print(merged_df.head())

    return merged_df


def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula los valores relativos de permit, long_gun y handgun respecto a la población total.

    Parameters:
        df (pd.DataFrame): El dataframe resultante del ejercicio 5.3.

    Returns:
        pd.DataFrame: El dataframe con las columnas permit_perc, longgun_perc y handgun_perc.
    """
    df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
    df['longgun_perc'] = (df['long_gun'] * 100) / df['pop_2014']
    df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']

    return df


def handle_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Maneja los outliers en el dataframe, específicamente el estado de Kentucky.

    Parameters:
        df (pd.DataFrame): El dataframe con los datos.

    Returns:
        pd.DataFrame: El dataframe con los outliers manejados.
    """
    # Calcular la media de permit_perc con dos decimales
    mean_permit_perc = round(df['permit_perc'].mean(), 2)
    print(f"Media de permit_perc (antes de manejar outliers): {mean_permit_perc}")

    # Mostrar toda la información relativa al estado de Kentucky
    kentucky_info = df[df['state'] == 'Kentucky']
    print("Información relativa al estado de Kentucky (antes de manejar outliers):")
    print(kentucky_info)

    # Reemplazar el valor permit_perc de Kentucky con la media de la columna
    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_perc

    # Volver a calcular la media de permit_perc con dos decimales
    new_mean_permit_perc = round(df['permit_perc'].mean(), 2)
    print(f"Media de permit_perc (después de manejar outliers): {new_mean_permit_perc}")

    # Mostrar la información actualizada del estado de Kentucky
    updated_kentucky_info = df[df['state'] == 'Kentucky']
    print("Información relativa al estado de Kentucky (después de manejar outliers):")
    print(updated_kentucky_info)

    # Conclusiones
    conclusiones = (
        "Antes de manejar los outliers:\n"
        "La media de permit_perc era 34.88.\n"
        "La información relativa al estado de Kentucky mostró un valor de permit_perc\n"
        "de 736.48, lo cual es extremadamente alto en comparación con otros estados.\n"
        "Después de manejar los outliers:\n"
        "Reemplazamos el valor de permit_perc de Kentucky con la media de la columna,\n"
        "que era 34.88. La media de permit_perc después de manejar los outliers se\n"
        "redujo a 21.12.\n"
        "Observaciones y conclusiones:\n"
        "Impacto de Kentucky como outlier: El estado de Kentucky tenía un valor de\n"
        "permit_perc extremadamente alto (736.48) antes de manejar los outliers.\n"
        "Este valor inflaba significativamente la media de permit_perc para todos los\n"
        "estados, haciendo que la media no representara adecuadamente el valor central\n"
        "de la distribución.\n"
        "Reducción de la media: Al reemplazar el valor de Kentucky con la media de\n"
        "permit_perc, la nueva media calculada fue 21.12, una reducción significativa\n"
        "desde la media original de 34.88. Esto indica que el valor atípico de Kentucky\n"
        "tenía un efecto distorsionador considerable en la media.\n"
        "Importancia del manejo de outliers: Los outliers pueden tener un impacto\n"
        "desproporcionado en las métricas estadísticas, distorsionando la interpretación\n"
        "de los datos. Al manejar los outliers, podemos obtener una representación más\n"
        "precisa y fiable de las métricas centrales, como la media. Este proceso es\n"
        "crucial para garantizar que los análisis y conclusiones derivados de los datos\n"
        "sean válidos y representativos de la mayoría de los casos.\n"
        "Efecto en los algoritmos de aprendizaje automático: Además de afectar las\n"
        "estadísticas descriptivas, los outliers pueden influir negativamente en el\n"
        "rendimiento de los modelos de aprendizaje automático, llevando a conclusiones\n"
        "erróneas y decisiones subóptimas. Por ello, el manejo adecuado de los outliers\n"
        "es esencial tanto en el análisis exploratorio de datos como en la modelización\n"
        "predictiva.\n"
        "Conclusión final: La gestión de valores atípicos como Kentucky es vital para\n"
        "obtener una visión precisa y no sesgada de los datos. En este caso, la reducción\n"
        "significativa en la media después de manejar el outlier confirma la importancia\n"
        "de este paso en el análisis de datos."
    )
    print(conclusiones)
    return df
