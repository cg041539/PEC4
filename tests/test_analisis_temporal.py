import pandas as pd
import tempfile
from src.analisis_temporal import time_evolution
import os

# Recreate the DataFrame from the provided image
data = {
    'year': [2020]*9,
    'state': ['Alabama', 'Alaska', 'California', 'Alabama', 'Alaska', 'California', 'Alabama', 'Alaska', 'California'],
    'permit': [31205, 143, 27792, 29633, 139, 32002, 37140, 223, 34694],
    'permit_rec': [606, 4, 0, 604, 10, 0, 510, 7, 0],
    'handgun': [34897, 4657, 81543, 24590, 2560, 35570, 22478, 2151, 34884],
    'long_gun': [17850, 3819, 48616, 12531, 1839, 22645, 12598, 1529, 22057]
}

df = pd.DataFrame(data)


def test_time_evolution_with_provided_data():
    # Crear un archivo temporal para guardar la gráfica
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    temp_file.close()

    try:
        # Llamar a la función time_evolution con el DataFrame proporcionado y el archivo temporal
        time_evolution(df, output_file=temp_file.name)

        # Verificar que el archivo se haya creado
        assert os.path.exists(temp_file.name), "El archivo de salida no fue creado."

        # Verificar que el archivo no esté vacío
        assert os.path.getsize(temp_file.name) > 0, "El archivo de salida está vacío."

        print("El test pasó exitosamente.")
    finally:
        # Eliminar el archivo temporal
        os.remove(temp_file.name)


# Ejecutar el test con los datos proporcionados
test_time_evolution_with_provided_data()
