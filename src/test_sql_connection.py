import pandas as pd
from sqlalchemy import create_engine

server = "ERNESTO_RIVERA"
database = "Manufactura"

connection_string = (
    "mssql+pyodbc://@{server}/{database}"  # Librería para conectar SQL
    "?driver=ODBC+Driver+17+for+SQL+Server"  # driver= puente que se usa para que se entiendan python y sql
    "&trusted_connection=yes"  # autenticación
).format(
    server=server, database=database
)  # rellena los huecos de los {}

engine = create_engine(connection_string)  # Motor para que funcione todo eso

df = pd.read_sql("SELECT TOP 5 * FROM dim_calendario", engine)
print(df)

# Prueba para ver si la conexión funcionaba
