import mysql.connector
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


def close_connection(connection):
    """Cierra la conexión a la base de datos."""
    if connection.is_connected():
        connection.close()
        print('Conexión cerrada')


if __name__ == "__main__":
    conn = create_connection()
    # Aquí puedes añadir el código para interactuar con la base de datos
    # Por ejemplo: realizar consultas, insertar datos, etc.
    if conn:
        close_connection(conn)