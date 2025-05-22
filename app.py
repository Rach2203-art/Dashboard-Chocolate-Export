```
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# URLs de los archivos CSV
clientes_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-ChocolateExport/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/TU_USUARIO/DashboardChocolate-Export/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/TU_USUARIO/DashboardChocolate-Export/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-ChocolateExport/main/barreras.csv"
clientes = pd.read_csv(clientes_url)
mercados = pd.read_csv(mercados_url)
exportaciones = pd.read_csv(exportaciones_url)
barreras = pd.read_csv(barreras_url)
