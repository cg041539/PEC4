import os
import pandas as pd
import folium
import json
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


def create_choropleth(data, geo_data, column, title):
    """
    Crea un mapa coroplético para una columna específica del dataframe.

    Parameters:
        data (pd.DataFrame): El dataframe con los datos.
        geo_data (dict): Los datos geojson para las fronteras de los estados.
        column (str): La columna del dataframe para la cual se crea el mapa.
        title (str): El título del mapa.

    Returns:
        folium.Map: El mapa generado.
    """
    m = folium.Map(location=[37.8, -96], zoom_start=4)
    folium.Choropleth(
        geo_data=geo_data,
        name='choropleth',
        data=data,
        columns=['code', column],
        key_on='feature.id',
        fill_color='YlGnBu',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=title
    ).add_to(m)
    folium.LayerControl().add_to(m)
    return m


def save_map_as_image(map_file, image_file):
    """
    Guarda un mapa folium como imagen usando Selenium.

    Parameters:
        map_file (str): La ruta del archivo HTML del mapa.
        image_file (str): La ruta del archivo donde se guardará la imagen.

    Outputs:
        None
    """
    # Configurar el servicio de GeckoDriver con la ruta específica
    service: Service = Service(executable_path='/snap/bin/firefox.geckodriver')
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(service=service, options=options)

    # Asegurarse de que el archivo existe antes de cargarlo
    file_url = f'file://{os.path.abspath(map_file)}'
    driver.get(file_url)
    time.sleep(5)  # Esperar a que se cargue el mapa

    # Guarda el screenshot del mapa
    screenshot = driver.get_screenshot_as_png()
    driver.quit()

    # Usa pillow para guardar el screenshot
    image = Image.open(BytesIO(screenshot))
    image.save(image_file)


def generate_and_save_maps(df):
    """
    Genera y guarda los mapas coropléticos para 'permit_perc', 'handgun_perc' y 'longgun_perc'.

    Parameters:
        df (pd.DataFrame): El dataframe con los datos procesados.

    Outputs:
        None
    """
    with open('./Data/us-states.json') as f:
        geojson_data = json.load(f)

    m1 = create_choropleth(df, geojson_data, 'permit_perc', 'Permit Percentage')
    m2 = create_choropleth(df, geojson_data, 'handgun_perc', 'Handgun Percentage')
    m3 = create_choropleth(df, geojson_data, 'longgun_perc', 'Long Gun Percentage')

    m1.save('permit_map.html')
    m2.save('handgun_map.html')
    m3.save('longgun_map.html')

    save_map_as_image('permit_map.html', 'permit_map.png')
    save_map_as_image('handgun_map.html', 'handgun_map.png')
    save_map_as_image('longgun_map.html', 'longgun_map.png')
