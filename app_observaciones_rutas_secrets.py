
import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
import json
from google.oauth2.service_account import Credentials

st.title("📋 Registro de Ruta Diaria - Llíria → UPV")

# Cargar las credenciales desde secrets
creds_dict = json.loads(st.secrets["GOOGLE_CREDS"])

# Autenticación con Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("Observaciones_Rutas_LLiria_UPV").sheet1

# Formulario
with st.form("formulario_ruta"):
    hora_salida = st.time_input("Hora de salida", value=datetime.now().time())
    dia_semana = st.selectbox("Día de la semana", ["lunes", "martes", "miércoles", "jueves", "viernes"])
    ruta = st.selectbox("Ruta utilizada", [
        "Ruta 1 - Empalme",
        "Ruta 2 - Benimàmet y Sant Joan",
        "Ruta 3 - Cantereria y La Granja",
        "Ruta 4 - Metrobus 136A directo",
        "Ruta 5 - 145 y tranvía desde SJ"
    ])
    problemas = st.text_input("¿Tuviste algún problema?")
    retraso_min = st.number_input("¿Cuántos minutos de retraso hubo?", min_value=0, max_value=120, value=0)
    transbordo_fallido = st.radio("¿Falló algún transbordo?", ["no", "sí"])
    comentarios = st.text_area("Comentarios adicionales")

    submitted = st.form_submit_button("Guardar observación")

# Guardar datos en Google Sheets
if submitted:
    nueva_fila = [
        datetime.now().strftime("%Y-%m-%d"),
        hora_salida.strftime("%H:%M"),
        dia_semana,
        ruta,
        problemas,
        str(retraso_min),
        transbordo_fallido,
        comentarios
    ]
    sheet.append_row(nueva_fila)
    st.success("✅ Observación guardada correctamente en Google Sheets.")
