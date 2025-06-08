import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
# Asegúrate de que 'vehicles_us.csv' esté en la misma carpeta que 'app.py'
try:
    car_data = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no se encuentra. Asegúrate de que esté en la misma carpeta que app.py.")
    st.stop() # Detiene la ejecución de la aplicación si el archivo no se encuentra

# Encabezado de la aplicación
st.header('Panel de Control de Anuncios de Vehículos')

# --- Controles para los gráficos ---

st.subheader('Opciones de Análisis:')

# Casilla de verificación para el histograma de kilometraje
build_odometer_histogram = st.checkbox('Mostrar Histograma de Kilometraje')

# Casilla de verificación para el gráfico de dispersión de precio vs kilometraje
build_price_odometer_scatter = st.checkbox('Mostrar Gráfico de Dispersión: Precio vs Kilometraje')

# NUEVOS: Casillas de verificación para análisis adicionales
st.markdown("---") # Separador visual
st.subheader('Análisis Adicional de Ventas:')

build_price_histogram = st.checkbox('Mostrar Histograma de Precios')
build_vehicle_type_bar = st.checkbox('Mostrar Conteo de Vehículos por Tipo')
build_price_condition_scatter = st.checkbox('Mostrar Gráfico de Dispersión: Precio vs Condición')


# --- Lógica para mostrar los gráficos ---

# Histograma de kilometraje
if build_odometer_histogram:
    st.write('Construyendo un histograma para el kilometraje de los coches...')
    fig_odometer_hist = px.histogram(car_data, x="odometer", title="Distribución de Kilometraje")
    st.plotly_chart(fig_odometer_hist, use_container_width=True)

# Gráfico de dispersión: Precio vs Kilometraje
if build_price_odometer_scatter:
    st.write('Construyendo un gráfico de dispersión de precio vs kilometraje...')
    fig_price_odometer_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs Kilometraje")
    st.plotly_chart(fig_price_odometer_scatter, use_container_width=True)


# NUEVOS GRÁFICOS:

# Histograma de Precios
if build_price_histogram:
    st.write('Construyendo un histograma para la distribución de precios...')
    fig_price_hist = px.histogram(car_data, x="price", title="Distribución de Precios")
    st.plotly_chart(fig_price_hist, use_container_width=True)

# Gráfico de Barras: Conteo de Vehículos por Tipo
if build_vehicle_type_bar:
    st.write('Contando vehículos por tipo...')
    # Contar las ocurrencias de cada tipo de vehículo
    vehicle_type_counts = car_data['type'].value_counts().reset_index()
    vehicle_type_counts.columns = ['Tipo de Vehículo', 'Cantidad']
    fig_type_bar = px.bar(vehicle_type_counts,
                          x='Tipo de Vehículo',
                          y='Cantidad',
                          title='Conteo de Anuncios por Tipo de Vehículo')
    st.plotly_chart(fig_type_bar, use_container_width=True)

# Gráfico de Dispersión: Precio vs Condición
if build_price_condition_scatter:
    st.write('Analizando precio vs condición de los vehículos...')
    # Para este gráfico, vamos a añadir color por tipo de vehículo para mayor detalle
    fig_price_condition_scatter = px.scatter(car_data,
                                            x="condition",
                                            y="price",
                                            color="type", # Colorea los puntos por tipo de vehículo
                                            title="Precio vs Condición del Vehículo por Tipo")
    st.plotly_chart(fig_price_condition_scatter, use_container_width=True)