import pyodbc
import pandas as pd

# Configura tu conexión con los parámetros de tu base de datos
server = 'SIQ-11WX2T3'  # Puede ser una dirección IP o nombre del servidor
database = 'SCADA'
username = 'sa'
password = 'siq123'

# Cadena de conexión ODBC
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

# Establecer la conexión
conn = pyodbc.connect(conn_str)

# Ejecutar una consulta SQL y convertir el resultado directamente a un DataFrame
query = 'SELECT * FROM Transaccion_neutralizacion'  # Tu consulta SQL aquí
df = pd.read_sql(query, conn)

import streamlit as st

st.title("Api Neutralización")

st.dataframe(df)

