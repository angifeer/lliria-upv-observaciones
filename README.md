
# Observaciones de rutas Llíria - UPV

Formulario en Streamlit para registrar la experiencia diaria de estudiantes que se desplazan desde Llíria a la Universitat Politècnica de València.

## Características

- Registro de retrasos y problemas
- Evaluación de fiabilidad de rutas
- Integración con Google Sheets

## Cómo usar

1. Añade un archivo `credentials.json` con tu clave de servicio de Google.
2. Crea una hoja de cálculo llamada `Observaciones_Rutas_LLiria_UPV` con estos encabezados en la primera fila:

```
fecha,hora_salida,dia_semana,ruta,problemas,retraso_min,transbordo_fallido,comentarios
```

3. Ejecuta la app con:

```bash
streamlit run app_observaciones_rutas.py
```

## Requisitos

Ver `requirements.txt`
