# Sports Streamlit App

Aplicación web desarrollada con Streamlit para el análisis de datos deportivos.

## Funcionalidades principales

- Login simple con usuario `admin` y contraseña `admin`
- Control de sesión con `st.session_state`
- Navegación lateral entre dos páginas
- Conexión a múltiples fuentes de datos:
  - Base de datos SQLite
  - API externa de equipos deportivos
- Visualización de datos en tablas
- Gráficos interactivos con Matplotlib
- Exportación de resultados a PDF
- Botón para imprimir la página
- Uso de caché para optimizar consultas

## Estructura del proyecto

```text
.streamlit/
common/
controllers/
data/
models/
pages/
.env
app.py
requirements.txt
README.md

Instalación
Clonar o descargar el proyecto

Instalar dependencias:
pip install -r requirements.txt

Inicializar la base de datos:
python models/init_db.py

Ejecutar la aplicación:
python -m streamlit run app.py