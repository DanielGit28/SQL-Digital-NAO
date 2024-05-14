#se requiere instalar previamente la librería
#pip install mysql-connector-python
import mysql.connector

# Conectarse a la base de datos MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="sql-digital-nao"
)

# Crear una tabla para almacenar los tweets
create_table_query = """
CREATE TABLE Tweets (
    id VARCHAR(255) PRIMARY KEY,
    texto TEXT,
    usuario VARCHAR(255),
    fecha DATETIME,
    retweets INT,
    favoritos INT
)
"""

# Ejecutra la consulta para crear la tabla
cursor = conn.cursor()
cursor.execute(create_table_query)

# Cerrar la conexión
conn.close()

print("Tabla creada exitosamente.")
