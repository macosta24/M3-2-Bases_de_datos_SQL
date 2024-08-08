import mysql.connector
import pandas as pd
from mysql.connector import Error


def create_connection():
    """Crea una conexión a la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host='195.179.238.58',  # Cambia esto a la dirección de tu servidor MySQL
            user='u927419088_admin',  # Cambia esto por tu nombre de usuario
            password='#Admin12345#',  # Cambia esto por tu contraseña
            database='u927419088_testing_sql'  # Cambia esto por el nombre de tu base de datos
        )

        if connection.is_connected():
            print('Conexión exitosa a la base de datos MySQL')
            return connection

    except Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None


def fetch_data_to_dataframe(connection):
    """Consulta los registros de la tabla curso y los convierte a un DataFrame de pandas."""
    try:
        query = "SELECT * FROM curso"
        df = pd.read_sql(query, connection)
        return df

    except Error as e:
        print(f'Error al ejecutar la consulta: {e}')
        return None


def export_to_excel(df, filename):
    """Exporta el DataFrame a un archivo Excel."""
    try:
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f'Datos exportados a {datosaExcel}')

    except Exception as e:
        print(f'Error al exportar a Excel: {e}')


if __name__ == "__main__":
    conn = create_connection()
    if conn:
        df = fetch_data_to_dataframe(conn)
        if df is not None:
            export_to_excel(df, 'cursos.xlsx')
        conn.close()