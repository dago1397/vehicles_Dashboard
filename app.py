import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Cuadro de mandos: anuncios de venta de coches en EE. UU.')
st.write('Explora el conjunto de datos de anuncios de vehículos usados mediante gráficos interactivos.')

# Vista previa de los datos
if st.checkbox('Mostrar vista previa de los datos'):
    st.dataframe(car_data.head(20))

# Histograma
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Creación de un histograma para la columna odómetro')
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig_hist, width='stretch')

# Gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')
if build_scatter:
    st.write('Creación de un gráfico de dispersión: odómetro vs. precio')
    fig_scatter = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig_scatter.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig_scatter, width='stretch')
