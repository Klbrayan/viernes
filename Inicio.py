import streamlit as st
import pandas as pd

# Set the page title and header
st.title("Proyecto de Valentino")


# Hero Section with image and project description (you can replace the image URL with your own)
st.image("https://yt3.ggpht.com/a/AATXAJyz5M1s0BIklx4_VoRyP6LrtygjFz7tbQjANw=s900-c-k-c0xffffffff-no-rj-mo", width=600)
st.write("Aquí tendremos varios temas interesantes en los cuales podremos hablar sobre nuestro proyecto integrador el cuál mencionamos varias cosas y tenemos una calculadora donde podemos calcular una liquidacion. Luego podemos ver un simulador de cesde que ayuda hacer varios filtros interesantes y por ultimas tenemos suicidios donde podemos ver informacion de esto ")

# Project Overview
st.subheader("Resumen del Proyecto")
st.write("- El proyecto de liquidacion veremos unos datos los cuales podemos almacenar y al final podemos usar una calculadora donde podemos hacer uso de calcular una liquidacion.")
st.write("- Proyecto simulador cesde. Esto puede ayudar mucho a los profesores o area administrativa para ver como van cada aulas con los docentes.")
st.write("- proyecto suicidios.Tenemos informacion sobre sitios y lugares donde ocurren más casos y codigos de suicidios.")

# Features and Benefits
st.subheader("Características y Beneficios")
st.write("**Cálculo Automatizado:** Reduce el tiempo dedicado al procesamiento manual de nóminas y minimiza errores.")
st.write("**Gestión de Impuestos:** Calcula automáticamente impuestos y deducciones conforme a las regulaciones vigentes.")
st.write("**Informes Detallados:** Genera informes precisos que proporcionan transparencia y facilitan la contabilidad.")
st.write("**No ayuda a tener una mayor claridad y facilidad a la hora de revisar datos. con más efetividad")

# Input Data Section
st.subheader("Ver informacion de algun datos CSV")
uploaded_file = st.file_uploader("Cargue el archivo CSV con los detalles de la nómina:", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Vista previa de los datos:")
    st.write(df.head())

# Payroll Processing Section
if st.button("Procesar Nómina"):
    if 'df' in locals():
        # Implement your payroll processing logic here
        # Example: Calculate salaries, taxes, deductions, bonuses, etc.
        st.write("¡La nómina ha sido procesada exitosamente!")
        # Display processed data or summary here
    else:
        st.warning("Por favor, cargue un archivo CSV primero.")



# Footer with team members and project information
st.subheader("Equipo y Contacto")
st.write("**Miembros del equipo:**")
st.write("-  1: Brayan Sneider Gomez Ortega.")
st.write("-  2: Alvaro Javier Martinez .")
st.write("-  3: Luis Ernesto Espinel Cano.")
st.write("-  3: Francisco José David Benítez.")

