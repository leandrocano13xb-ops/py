import os
import warnings
import pandas as pd
import pyodbc
from dotenv import load_dotenv

# Ignorar advertencias innecesarias
warnings.filterwarnings('ignore')

# Cargar variables del archivo .env
load_dotenv()

# Conexión a la base de datos usando la información del .env
def conexion_db():
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    driver = os.getenv('DB_DRIVER')
    
    conn_str = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    return pyodbc.connect(conn_str)

# Ejemplo de consulta usando pandas y pyodbc
try:
    conn = conexion_db()
    query = "SELECT * FROM clientes;"
    df_clientes = pd.read_sql(query, conn)
    print("Conexión exitosa. Primeros registros:")
    print(df_clientes.head())
    conn.close()
except Exception as e:
    print(f"Error en la conexión o consulta: {e}")