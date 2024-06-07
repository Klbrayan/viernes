import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Set the page title and header
st.title("Simulador de Datos de Intentos de Suicidio")

# Load the dataset
df = pd.read_csv('static/datasets/sivigila_intsuicidio.csv')

# Convert necessary columns to strings to avoid type errors during sorting
df['cod_eve'] = df['cod_eve'].astype(str)
df['semana'] = df['semana'].astype(str)
df['año'] = df['año'].astype(str)
df['sexo_'] = df['sexo_'].astype(str)
df['ocupacion_'] = df['ocupacion_'].astype(str)
df['tip_ss_'] = df['tip_ss_'].astype(str)
df['per_etn_'] = df['per_etn_'].astype(str)

# Get unique values for select columns
cod_eveU = sorted(df['cod_eve'].unique())
semanaU = sorted(df['semana'].unique())
añoU = sorted(df['año'].unique())
sexoU = sorted(df['sexo_'].unique())
ocupacionU = sorted(df['ocupacion_'].unique())
tip_ssU = sorted(df['tip_ss_'].unique())
per_etnU = sorted(df['per_etn_'].unique())

# -----------------------------------------------------------------------------------
def filtro1():
    col1, col2 = st.columns(2)
    with col1:
        cod_eve_valid = [eve for eve in cod_eveU if not df[(df['cod_eve'] == eve)].empty]
        cod_eve = st.selectbox("Código de Evento", cod_eve_valid)
    with col2:
        año_valid = [a for a in añoU if not df[(df['cod_eve'] == cod_eve) & (df['año'] == a)].empty]
        año = st.selectbox("Año", año_valid)
    
    resultado = df[(df['cod_eve'] == cod_eve) & (df['año'] == año)]
    resultado = resultado.reset_index(drop=True)
    
    # Grafico de barras - Número de casos por semana
    fig = px.bar(resultado, x='semana', y='cod_eve', title="Número de Casos por Semana",
                 labels={'semana': 'Semana', 'cod_eve': 'Número de Casos'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabla
    st.table(resultado[['semana', 'cod_eve', 'año', 'sexo_', 'edad_', 'ocupacion_']])

# -----------------------------------------------------------------------------------
def filtro2():
    col1, col2, col3 = st.columns(3)
    with col1:
        semana_valid = [sem for sem in semanaU if not df[(df['semana'] == sem)].empty]
        semana = st.selectbox("Semana", semana_valid)
    with col2:
        sexo_valid = [s for s in sexoU if not df[(df['semana'] == semana) & (df['sexo_'] == s)].empty]
        sexo = st.selectbox("Sexo", sexo_valid)
    with col3:
        ocupacion_valid = [occ for occ in ocupacionU if not df[(df['semana'] == semana) & (df['sexo_'] == sexo) & (df['ocupacion_'] == occ)].empty]
        ocupacion = st.selectbox("Ocupación", ocupacion_valid)

    resultado = df[(df['semana'] == semana) & (df['sexo_'] == sexo) & (df['ocupacion_'] == ocupacion)]
    resultado = resultado.reset_index(drop=True)
    
    # Grafico de barras - Distribución de edades
    fig = px.histogram(resultado, x='edad_', title="Distribución de Edades",
                       labels={'edad_': 'Edad', 'cod_eve': 'Número de Casos'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabla
    st.table(resultado[['semana', 'cod_eve', 'sexo_', 'edad_', 'ocupacion_', 'tip_ss_']])

# -----------------------------------------------------------------------------------
def filtro3():
    col1, col2 = st.columns(2)
    with col1:
        tip_ss_valid = [tip for tip in tip_ssU if not df[(df['tip_ss_'] == tip)].empty]
        tip_ss = st.selectbox("Tipo de Seguridad Social", tip_ss_valid)
    with col2:
        per_etn_valid = [per for per in per_etnU if not df[(df['tip_ss_'] == tip_ss) & (df['per_etn_'] == per)].empty]
        per_etn = st.selectbox("Pertenencia Étnica", per_etn_valid)
    
    resultado = df[(df['tip_ss_'] == tip_ss) & (df['per_etn_'] == per_etn)]
    resultado = resultado.reset_index(drop=True)
    
    # Grafico de barras - Distribución de edades por tipo de seguridad social y pertenencia étnica
    fig = px.histogram(resultado, x='edad_', title="Distribución de Edades por Tipo de Seguridad Social y Pertenencia Étnica",
                       labels={'edad_': 'Edad', 'cod_eve': 'Número de Casos'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabla
    st.table(resultado[['semana', 'cod_eve', 'año', 'sexo_', 'edad_', 'ocupacion_', 'per_etn_']])

# -----------------------------------------------------------------------------------
# Main application
st.sidebar.title("Filtros")
filtro_seleccionado = st.sidebar.selectbox("Seleccione un Filtro", ["Filtro por Código de Evento y Año", "Filtro por Semana, Sexo y Ocupación", "Filtro por Tipo de Seguridad Social y Pertenencia Étnica"])

if filtro_seleccionado == "Filtro por Código de Evento y Año":
    filtro1()
elif filtro_seleccionado == "Filtro por Semana, Sexo y Ocupación":
    filtro2()
else:
    filtro3()
