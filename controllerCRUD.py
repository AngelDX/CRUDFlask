from db import conexionDB

def create_client(nombres,apellidos,dni,direccion,email):
    conexion = conexionDB()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO clientes(nombres,apellidos,dni,direccion,email) VALUES (%s,%s,%s,%s,%s)",
                       (nombres,apellidos,dni,direccion,email))
    conexion.commit()
    conexion.close()


def get_clients():
    conexion = conexionDB()
    clientes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
    conexion.close()
    return clientes


def delete_client(id):
    conexion = conexionDB()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def get_by_id(id):
    conexion = conexionDB()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM clientes WHERE id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def update_client (nombres, apellidos,dni,direccion,email,id):
    conexion = conexionDB()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET nombres=%s,apellidos=%s,dni=%s,direccion=%s,email=%s WHERE id = %s",
                       (nombres,apellidos,dni,direccion,email))
    conexion.commit()
    conexion.close()