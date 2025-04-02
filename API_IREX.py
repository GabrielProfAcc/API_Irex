import streamlit as st
import pyodbc
import pandas as pd

st.set_page_config(page_title="Api Neutralización", page_icon="🌟")  # Configura el título de la página y el icono

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()


query = "SELECT * from Transaccion_neutralizacion"
df = pd.read_sql(query, conn)

import streamlit as st
import pandas as pd

# Título y cabecera
from streamlit_extras.dataframe_explorer import dataframe_explorer
#----------------------------------------------------------------------------------
st.header("API neutralización", divider=True)


filtered_df = dataframe_explorer(df, case=False)
st.dataframe(filtered_df, use_container_width=True)