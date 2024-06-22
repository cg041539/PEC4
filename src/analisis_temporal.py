import pandas as pd
import matplotlib.pyplot as plt


def time_evolution(df: pd.DataFrame, output_file: str = 'time_evolution.png') -> None:
    """
    Crea un gráfico de la evolución temporal de permit, hand_gun y long_gun.

    Parameters:
        df (pd.DataFrame): El dataframe con los datos.
        output_file (str): La ruta del archivo donde se guardará la gráfica.

    Outputs:
        None
    """
    yearly_totals = df.groupby('year')[['permit', 'handgun', 'long_gun']].sum()

    plt.figure(figsize=(10, 6))
    plt.plot(yearly_totals.index, yearly_totals['permit'], label='Permit')
    plt.plot(yearly_totals.index, yearly_totals['handgun'], label='Handgun')
    plt.plot(yearly_totals.index, yearly_totals['long_gun'], label='Long Gun')

    plt.xlabel('Año')
    plt.ylabel('Cantidad')
    plt.title('Evolución Temporal de Permits, Handguns y Long Guns')
    plt.legend()
    plt.grid(True)

    # Guardar la gráfica en un archivo
    plt.savefig(output_file)
    print(f"Gráfica guardada como {output_file}")

    # Conclusiones
    conclusiones = (
        "En el fichero que nos dan solo hay 3 meses del 2020 por lo que no se puede "
        "concluir mucho aunque parece que la tendencia es de bajada tanto en permisos "
        "como en los dos tipos de armas desde un máximo del 2016. Pero si buscamos los "
        "datos más actualizados hasta 2023, encontramos que quizás por el efecto "
        "pandemia se cambia la tendencia. Aunque sin incrementarse los permisos porque "
        "tampoco creo que fuera muy accesible realizar las pruebas, se llega a máximos "
        "de número de armas cortas y largas, superándose 2016. Supongo que por el "
        "efecto pandemia es lógico que esto pase en un país como USA. La tendencia "
        "después de pandemia es de bajada en los dos tipos de armas, pero en permisos "
        "aumenta sin llegar a las cifras de 2016 y solo en 2023 se observa una ligera "
        "bajada en permisos."
    )
    print(conclusiones)
