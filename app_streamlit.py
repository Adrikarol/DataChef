import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as c
import pickle

st.set_page_config(page_title="DataChef",
                   page_icon=":electric_plug:")

color_de_fondo = "#363636"

seleccion = st.sidebar.radio("Menú", ['Introducción', 'Limpieza de datos', 'Análisis de datos', 'Predicciones', "Conclusiones"], index=0)

if seleccion == "Introducción":
# if opcion_introduccion:
    img = Image.open("./Media/header.png")
    imagen = img.resize((800, 300))
    st.image(imagen)
    texto = """
                En un mercado gastronómico cada vez más competitivo, el éxito de un restaurante se sustenta en la eficiencia y la rentabilidad. 
                La intuición y la experiencia tradicionales ya no bastan en este entorno. 
                Para destacarse, los restaurantes deben valerse de herramientas que les permitan tomar decisiones estratégicas respaldadas por datos concretos. 
                El análisis de datos y la implementación de modelos predictivos se vuelven imprescindibles en este contexto. 
                Estas tecnologías innovadoras ofrecen una perspectiva hacia el futuro al proporcionar información valiosa sobre el comportamiento de los clientes, las tendencias del mercado y el rendimiento del negocio. 
                El propósito de este proyecto de análisis de datos es aprovechar estas tecnologías para optimizar las operaciones y estrategias de ventas del restaurante, aumentando su eficiencia y rentabilidad. 
                A través de un minucioso análisis de los datos disponibles, se identificarán áreas de mejora, se desarrollarán modelos predictivos para la demanda y la toma de decisiones, y se personalizará la experiencia del cliente."""
    st.write(texto)

elif seleccion == "Limpieza de datos":

    texto = """Obtenemos los datos con los que el restaurante cuenta actualmente, a través de la API con la que el local trabaja.
                Podemos ver la estructura que tenian en ese momento:
            """
    st.write(texto)

    with st.expander('Datos sin procesar'):
        df = pd.read_csv("./base_de_datos/archivos_csv/ventas_historico.csv")
        st.write(df) 
  
    texto ="""Creación de tablas y relaciones:
              Mediante cambios en la estructura de los datos, se definieron distintas tablas en las que dividimos los registros, para su escalabilidad.
              De esta manera la base de datos no solo es más eficiente y optimiza el rendimiento, sino que permite hacer análisis más detallados de algunos puntos importantes, como las ventas por productos."""
    st.write(texto)


    with st.expander('Tabla jerarquias'):
        df = pd.read_csv("./base_de_datos/archivos_csv/hierarchy_v2.csv")
        st.write(df)

    with st.expander('Tabla productos'):
        df = pd.read_csv("./base_de_datos/archivos_csv/product_v2.csv")
        st.write(df)

    with st.expander('Tabla ventas por productos'):
        df = pd.read_csv("./base_de_datos/archivos_csv/ventaxproducts_v2.csv")
        st.write(df)

    with st.expander('Tabla meseros'):
        df = pd.read_csv("./base_de_datos/archivos_csv/meseros.csv")
        st.write(df)

    with st.expander('Tabla mesas'):
        df = pd.read_csv("./base_de_datos/archivos_csv/mesas.csv")
        st.write(df)    

    with st.expander('Tabla formas de pago'):
        df = pd.read_csv("./base_de_datos/archivos_csv/tipos_forma_pago.csv")
        st.write(df)       

    with st.expander('Tabla ventas por forma de pago'):
        df = pd.read_csv("./base_de_datos/archivos_csv/forma_pago.csv")
        st.write(df)

    with st.expander('Tabla ordenes'):
        df = pd.read_csv("./base_de_datos/archivos_csv/orders.csv")
        st.write(df)

    with st.expander('Tabla información sobre ordenes'):
        df = pd.read_csv("./base_de_datos/archivos_csv/orders_info.csv")
        st.write(df)     


    texto ="""Relaciones entre las distintas tablas:"""
    st.write(texto)    

    with st.expander('Relaciones'):
        img = Image.open("./Media/diagrama.png")
        imagen = img.resize((800, 400))
        st.image(imagen)    

elif seleccion == "Análisis de datos":

    st.write("## Análisis de datos")

    st.write("<iframe width='1000' height='600' src='https://app.powerbi.com/view?r=eyJrIjoiYjdhODEwYTYtM2YxMS00YTQ5LTg1ZjMtNGM5MTA5YmEwM2Y5IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9' style='display:block;margin:auto;'></iframe>", unsafe_allow_html=True)

elif seleccion == "Predicciones":
    pass


elif seleccion == "Conclusiones":
    texto ="""1. Tendencias de ingresos y estacionalidad:

    - El año 2023 fue el de mayor ingreso total con $476.081.246,00, seguido por 2022, 2021 y 2024 en orden descendente.

    - Los ingresos en 2023 fueron superiores en un 3.33% en comparación con 2022.

    - Se observa un patrón estacional en los ingresos, siendo los primeros trimestres (entre octubre y marzo) los más altos, coincidiendo con las estaciones de primavera y verano. Esto sugiere oportunidades para lanzar promociones o aumentar el marketing durante estos períodos para aprovechar la mayor demanda.



    2. Ventas locales vs. online:

    - En 2023, las ventas locales representaron el 63.01% mientras que las ventas online fueron el 37,01%. En 2022, estos porcentajes fueron del 45.48% y 54.54% respectivamente.

    - Esta tendencia indica un aumento en la preferencia por las ventas locales en 2023 en comparación con 2022. Se podrían explorar estrategias para fortalecer las ventas online, como mejorar la experiencia del usuario en la plataforma de pedidos en línea o promociones específicas para este canal.



    3. Métodos de pago:

    - En 2022 y 2023, los métodos de pago más utilizados fueron tarjeta débito, tarjeta crédito y Uber Eats.

    - Se observa un aumento significativo en el uso de tarjeta débito como método de pago preferido en 2023 en comparación con 2022.

    - Esto sugiere la necesidad de asegurar la disponibilidad de opciones de pago electrónico y posiblemente implementar incentivos para promover ciertos métodos de pago que sean más beneficiosos para el restaurante, como tarjetas de débito que pueden reducir las tarifas de transacción.



    4. Tipos de productos vendidos:

    - La categoría "Bar" tuvo la mayor cantidad de ventas, representando el 26,80% del total, seguida por "Schops" y "Fries".

    - Existe una correlación positiva entre la cantidad vendida y la facturación total, lo que indica que los productos más vendidos también generan mayores ingresos.

    - Se podrían impulsar estrategias para promocionar los productos más populares y aumentar la visibilidad de otras categorías para equilibrar las ventas y maximizar los ingresos.
    """
    st.write(texto) 