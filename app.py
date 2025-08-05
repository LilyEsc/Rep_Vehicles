import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('C:/Users/hp/Documents/ProyectoSprint7/Rep_Vehicles/vehicles_data.csv')

st.title('Proyecto Sprint 7. Analisis sobre venta de autos')

st.header('Dataset de Vehiculos')
st.dataframe(car_data)

hist_button = st.checkbox('Construir histograma')

if hist_button: #al hacer click en el botón
    st.write(f'Histograma por rango de precios de los vehiculos')
    fig = px.histogram(car_data, x='price')
    st.plotly_chart(fig, use_container_width=True)

barra_button = st.checkbox('Constriur Gráfico de Barras')

if barra_button:
    tipo_auto = car_data.groupby(by='type')['price'].agg('count')
    tipo_auto = tipo_auto.reset_index()
    st.write('Creación de un Gráfico de Barras para los diferente tipos de carroceria')
    fig = px.bar(tipo_auto, x='type', y='price', color='type')
    st.plotly_chart(fig, use_container_width=True)

marcas = ['ford', 'chevrolet', 'toyota', 'nissan', 'hyundai']
marca_select = st.selectbox('Seleccione una marca:', options=marcas)