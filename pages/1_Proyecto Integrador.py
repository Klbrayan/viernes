import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import date

# Configuración de la página
st.set_page_config(layout="wide")
st.title("Demandantes en Oficina Pública de Empleo")

# Cargar el archivo CSV
file_path = 'static/datasets/demantantes_en_oficina_publica_de_empleo.csv'
df = pd.read_csv(file_path)

# Reemplazar valores nulos para evitar errores en las selecciones
df = df.fillna("No especificado")

# Obtener valores únicos para cada filtro
municipios = sorted(df['municipio'].unique())
actividades = sorted(df['actividad_principal'].unique())
cargos = sorted(df['cargo_del_solicitante'].unique())
clasificaciones = sorted(df['clasificación_de_la_empresa'].unique())
sectores = sorted(df['sector_económico'].unique())

# -----------------------------------------------------------------------------------
def filtro1():
    col1, col2 = st.columns(2)
    with col1:
        municipio = st.selectbox("Municipio", municipios)
    with col2:
        actividades_filtradas = df[df['municipio'] == municipio]['actividad_principal'].unique()
        actividad = st.selectbox("Actividad Principal", actividades_filtradas)
    
    resultado = df[(df['municipio'] == municipio) & (df['actividad_principal'] == actividad)]
    resultado = resultado.reset_index(drop=True)
    
    if not resultado.empty:
        # Gráfico de barras
        fig = go.Figure(data=[
            go.Bar(name='Cargo del Solicitante', x=resultado['cargo_del_solicitante'].value_counts().index, y=resultado['cargo_del_solicitante'].value_counts().values),
            go.Bar(name='Clasificación de la Empresa', x=resultado['clasificación_de_la_empresa'].value_counts().index, y=resultado['clasificación_de_la_empresa'].value_counts().values),
            go.Bar(name='Sector Económico', x=resultado['sector_económico'].value_counts().index, y=resultado['sector_económico'].value_counts().values)
        ])
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)
    
        # Tabla
        st.table(resultado[["municipio", "actividad_principal", "cargo_del_solicitante", "clasificación_de_la_empresa", "sector_económico"]])
    else:
        st.warning("No se encontraron datos para los filtros seleccionados.")

# -----------------------------------------------------------------------------------
def filtro2():
    col1, col2, col3 = st.columns(3)
    with col1:
        municipio = st.selectbox("Municipio", municipios)
    with col2:
        actividades_filtradas = df[df['municipio'] == municipio]['actividad_principal'].unique()
        actividad = st.selectbox("Actividad Principal", actividades_filtradas)
    with col3:
        cargos_filtrados = df[(df['municipio'] == municipio) & (df['actividad_principal'] == actividad)]['cargo_del_solicitante'].unique()
        cargo = st.selectbox("Cargo del Solicitante", cargos_filtrados)

    resultado = df[(df['municipio'] == municipio) & (df['actividad_principal'] == actividad) & (df['cargo_del_solicitante'] == cargo)]
    resultado = resultado.reset_index(drop=True)
    
    if not resultado.empty:
        # Gráfico de barras
        fig = go.Figure(data=[
            go.Bar(name='Clasificación de la Empresa', x=resultado['clasificación_de_la_empresa'].value_counts().index, y=resultado['clasificación_de_la_empresa'].value_counts().values),
            go.Bar(name='Sector Económico', x=resultado['sector_económico'].value_counts().index, y=resultado['sector_económico'].value_counts().values)
        ])
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        # Tabla
        st.table(resultado[["municipio", "actividad_principal", "cargo_del_solicitante", "clasificación_de_la_empresa", "sector_económico"]])
    else:
        st.warning("No se encontraron datos para los filtros seleccionados.")

# -----------------------------------------------------------------------------------
def calculadora_liquidacion():
    st.header("Calculadora de Liquidación")
    
    salario = st.number_input("Salario mensual ($)", min_value=0)
    fecha_inicio = st.date_input("Fecha de inicio de contrato")
    fecha_fin = st.date_input("Fecha de fin de contrato")

    if st.button("Calcular Liquidación"):
        # Calcular días trabajados
        dias_trabajados = (fecha_fin - fecha_inicio).days
        años_trabajados = dias_trabajados / 365.25

        # Calcular componentes de la liquidación
        cesantias = salario * años_trabajados
        intereses_cesantias = cesantias * 0.12 * años_trabajados
        prima_servicios = salario * años_trabajados
        vacaciones = salario * años_trabajados / 2

        # Mostrar resultados
        st.write("### Resultados de la Liquidación:")
        st.write(f"**Cesantías:** ${cesantias:,.2f}")
        st.write(f"**Intereses sobre cesantías:** ${intereses_cesantias:,.2f}")
        st.write(f"**Prima de servicios:** ${prima_servicios:,.2f}")
        st.write(f"**Vacaciones:** ${vacaciones:,.2f}")

        total_liquidacion = cesantias + intereses_cesantias + prima_servicios + vacaciones
        st.write(f"### Total Liquidación: ${total_liquidacion:,.2f}")

# -----------------------------------------------------------------------------------
filtros = [
    "Filtro por Municipio y Actividad",
    "Filtro por Municipio, Actividad y Cargo",
    "Calculadora de Liquidación"
]

filtro = st.selectbox("Filtros", filtros)

if filtro:
    filtro_index = filtros.index(filtro)

    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()
    elif filtro_index == 2:
        calculadora_liquidacion()
