# Programación para la Ciencia de Datos - PEC4

## Descripción

Este proyecto contiene la solución a la cuarta prueba de evaluación continua (PEC) de la asignatura Programación para la Ciencia de Datos. El proyecto incluye funciones para leer, limpiar y analizar datos de verificaciones de antecedentes para la compra de armas de fuego en los Estados Unidos.

## Estructura del Proyecto

```plaintext
PEC4/
│
├── Data/
│   ├── nics-firearm-background-checks.csv
│   ├── us-state-populations.csv
│   └── us-states.json
│
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── data_processing.py
│   ├── agrupar.py
│   ├── analisis_temporal.py
│   ├── analisis_estados.py
│   └── mapas.py
│
├── venv/ # (Carpeta del entorno virtual)
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_data_cleaning.py
│   ├── test_data_processing.py
│   ├── test_agrupar.py
│   ├── test_analisis_temporal.py
│   ├── test_analisis_estados.py
│   └── test_mapas.py
│
├── main.py
├── README.md
├── requeriments.txt
└── license.txt
```

## Requisitos
- Python 3.6+
- pip (gestor de paquetes de Python)
- virtualenv (opcional, pero recomendado)

## Instalación y Configuración
1. Clona este repositorio:
```bash
git clone https://github.com/cg041539/PEC4.git
cd PEC4
```

2. (Opcional) Crea y activa un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate
```

3. Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

4. Instala el paquete en modo editable:
```bash
pip install -e .
```

## Ejecución del Proyecto
### Ejecutar Todas las Funciones
Para ejecutar todas las funciones de la PEC:
```bash
pec4
```

## Ejecutar un modulo
```bash
python main.py --module [nombre_del_modulo]
```

### Ejecutar una Función Específica

Para ejecutar una función específica dentro de un módulo,

```bash
pec4 --module [nombre_del_modulo] --function [nombre_de_la_funcion] --file_path [ruta_del_archivo]
```

### Opciones disponibles:
- **`--module`**: 
  - 'data_cleaning'
  - 'data_processing'
  - 'agrupar'
  - 'analisis_temporal'
  - 'analisis_estados'
  - 'generate_and_save_maps'
- **`--function`**: 
  - 'read_csv'
  - 'clean_csv'
  - 'rename_col'
  - 'breakdown_date'
  - 'erase_month'
  - 'groupby_state_and_year'
  - 'print_biggest_handguns'
  - 'print_biggest_longguns'
  - 'time_evolution'
  - 'groupby_state'
  - 'clean_states'
  - 'merge_datasets'
  - 'calculate_relative_values'
  - 'handle_outliers'
- **`--file_path`**: Ruta al archivo CSV (opcional). Por defecto, usa './Data/nics-firearm-background-checks.csv'. También puede leer una URL, por ejemplo: 
  - [nics-firearm-background-checks.csv](https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv)
  - Archivo con datos hasta 2023: './Data/nics-firearm-background-checks_2023.csv'

# Ejemplos

## Data Cleaning

Para ejecutar el módulo completo
```bash
python main.py --module data_cleaning
```

Por ejemplo, para ejecutar solo read_csv en el módulo data_cleaning:

```bash
python main.py --module data_cleaning --function read_csv --file_path https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv
```
Para ejecutar solo clean_csv en el módulo data_cleaning

```bash
python main.py --module data_cleaning --function clean_csv
```
Para renombrar columnas:
```bash
python main.py --module data_cleaning --function rename_col
```

## Data Processing

Para ejecutar el módulo completo
```bash
python main.py --module data_processing
```

Para dividir la columna month en year y month:
```bash
python main.py --module data_processing --function breakdown_date
```
Para eliminar la columna month:
```bash
python main.py --module data_processing --function erase_month
```



## Descripción de los Módulos y Funciones

### Módulo `data_cleaning.py`

Este módulo contiene las siguientes funciones:

#### `read_csv` Function

`read_csv(file_path: str) -> pd.DataFrame`

**Descripción:** Lee el archivo CSV y muestra las primeras cinco filas y la estructura del dataframe.

**Inputs:**
- `file_path` - La ruta del archivo CSV o de la url.

**Outputs:**
- `df` Devuelve el dataframe leído.

### `clean_csv` Function

`clean_csv(df: pd.DataFrame) -> pd.DataFrame`

**Descripción:** Limpia el dataframe, eliminando todas las columnas excepto `month`, `state`, `permit`, `handgun`, y `long_gun`.

**Inputs:**
- `df` - El dataframe a limpiar.

**Outputs:**
- `df` - Devuelve el dataframe limpio con solo las columnas especificadas.

### `rename_col` Function

`rename_col(df: pd.DataFrame) -> pd.DataFrame`

**Descripción:** La función `rename_col` se utiliza para renombrar una columna específica de un DataFrame de pandas. En este caso, la columna `'long_gun'` se renombra a `'longgun'`. La función también imprime un mensaje indicando si la columna fue renombrada y muestra los nombres de todas las columnas en el DataFrame resultante.

**Inputs:**
- `df` (pd.DataFrame) - El DataFrame original que contiene los datos. Es necesario que tenga una columna llamada `'long_gun'` para que el renombramiento se realice.

**Outputs:**
- `pd.DataFrame` - El DataFrame con la columna renombrada. Si la columna `'long_gun'` no existe, se devuelve el DataFrame original sin cambios.

### Descripción
La función `rename_col` se utiliza para renombrar una columna específica de un DataFrame de pandas. En este caso, la columna `'long_gun'` se renombra a `'longgun'`. La función también imprime un mensaje indicando si la columna fue renombrada y muestra los nombres de todas las columnas en el DataFrame resultante.

### Inputs
- `df` (pd.DataFrame): El DataFrame original que contiene los datos. Es necesario que tenga una columna llamada `'long_gun'` para que el renombramiento se realice.

### Outputs
- `pd.DataFrame`: El DataFrame con la columna renombrada. Si la columna `'long_gun'` no existe, se devuelve el DataFrame original sin cambios.

# Módulo `data_processing.py`

Este módulo contiene las siguientes funciones:

## `breakdown_date` Function

`breakdown_date(df: pd.DataFrame) -> pd.DataFrame`

### Descripción

La función `breakdown_date` se utiliza para dividir la información de la columna `'month'` en dos nuevas columnas: `'year'` y `'month'`. La columna `'month'` debe contener datos en el formato `'YYYY-MM'`. La función convierte estos datos en columnas separadas para el año y el mes, y se asegura de que ambos sean de tipo entero. También imprime las primeras cinco filas del DataFrame después de realizar la división para verificación.

### Inputs

- `df` (pd.DataFrame): El DataFrame de entrada que contiene una columna llamada `'month'` con fechas en el formato `'YYYY-MM'`.

### Outputs

- `pd.DataFrame`: El DataFrame con la información de la columna `'month'` dividida en dos nuevas columnas: `'year'` y `'month'`.

## `erase_month` Function

`erase_month(df: pd.DataFrame) -> pd.DataFrame`

### Descripción

La función `erase_month` se utiliza para eliminar la columna `'month'` de un DataFrame de pandas. Si la columna `'month'` existe en el DataFrame, será eliminada. La función también imprime las primeras cinco filas del DataFrame después de la eliminación de la columna para verificación y lista las columnas actuales del DataFrame.

### Inputs

- `df` (pd.DataFrame): El DataFrame de entrada que puede contener una columna llamada `'month'`.

### Outputs

- `pd.DataFrame`: El DataFrame sin la columna `'month'`.

# Módulo `agrupar`

Este módulo contiene las siguientes funciones:

## `groupby_state_and_year` Function

`groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame`

### Descripción

La función `groupby_state_and_year` agrupa los datos de un DataFrame por `'year'` y `'state'` y calcula los valores acumulados para cada grupo. Esta función es útil para resumir datos anuales por estado.

### Inputs

- `df` (pd.DataFrame): DataFrame con las columnas `'year'` y `'state'`, y otras columnas numéricas que serán sumadas durante la agrupación.

### Outputs

- `pd.DataFrame`: DataFrame agrupado por `'year'` y `'state'` con valores acumulados.

# MAIN

## `main.py`

Este script es el punto de entrada principal para ejecutar el proyecto. Contiene las siguientes funcionalidades:

- **Ejecución Completa:** Ejecuta todas las funciones de la PEC si no se proporcionan argumentos específicos.
- **Ejecución Específica:** Permite ejecutar una función específica dentro de un módulo usando los argumentos `--module` y `--function`.

# Notas

Asegúrate de tener todas las dependencias instaladas en el entorno virtual.

Los archivos necesarios deben estar en el directorio `Data`.

# Testeo

## Ejecutar Tests

Para ejecutar los tests, utiliza `pytest`. Asegúrate de estar en el directorio raíz del proyecto.

Para el módulo de mapas no se han generado tests porque ya se ve que los archivos se crean.

```bash
pytest tests/test_data_cleaning.py # Ejecutar un test especifico
pytest tests/ # Ejecutar todos los tests
```

## Verificar la Cobertura de los Tests

Instalar `coverage`:
```bash
pip install coverage
```

Ejecutar los tests con cobertura:
```bash
coverage run -m pytest
```

Generar el informe de cobertura en la terminal:
```bash
coverage report
```

Generar el informe HTML y abrirlo en el navegador:
```bash
coverage html
open htmicov/index.html
```

Con estos pasos, podemos ver el porcentaje de cobertura de tus tests y obtener un informe detallado de qué partes de tu código están cubiertas por los tests y cuáles no.

# Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE.txt`.