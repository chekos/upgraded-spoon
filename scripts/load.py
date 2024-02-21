import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector
import os 

# Conexión a Snowflake
conn = snowflake.connector.connect(
    user=os.environ['SNOWSQL_USER'],
    password=os.environ['SNOWSQL_PWD'],
    account=os.environ['SNOWSQL_ACCOUNT'],
    warehouse='COMPUTE_WH',
    database='SOURCE',
    schema='RAW'
)

# Asumiendo que 'users_data.json' es el archivo con los datos extraídos
df = pd.read_json('users_data.json')

# Crear cursor
cur = conn.cursor()

# Cargar el DataFrame en la tabla de Snowflake
write_pandas(conn, df, 'cf_usuarios')

print("DataFrame cargado en Snowflake.")

# Cerrar la conexión
cur.close()
conn.close()
