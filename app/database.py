import pymysql
import base64

DATABASE_CONFIG = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '',
    'database' : 'Sleepcraft'
}

def crear_tablas():
    try:
        conn = pymysql.connect(**DATABASE_CONFIG)
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS tipoUsuario (
                id INT AUTO_INCREMENT PRIMARY KEY,
                tipo VARCHAR(50)
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS usuario (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50),
                correo VARCHAR(50),
                contrasena VARCHAR(255),
                telefono VARCHAR(50),
                ciudad VARCHAR(50),
                direccion VARCHAR(50),
                idTipoUsuario INT,
                FOREIGN KEY (idTipoUsuario) REFERENCES tipoUsuario (id)
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS codigo (
                id INT AUTO_INCREMENT PRIMARY KEY,
                codigo VARCHAR(50)
            )
            """
        )
        # Pre-cargar datos en tipoUsuario
        cur.execute(
            """
            INSERT IGNORE INTO tipoUsuario (tipo)
            VALUES ('administrador');
            """
        )
        cur.execute(
            """
            INSERT IGNORE INTO codigo (codigo)
            VALUES ('123213jncjnvsvd');
            """
        )
        cur.execute(
            """
            INSERT IGNORE INTO tipoUsuario (tipo)
            VALUES ('cliente');
            """
        )
        conn.commit()
        mensaje = "TODO ANDO BIEN"
    except BaseException as error:
        mensaje =  f"NO ANDA PORQUE {error}"
    finally:
        cur.close()
        conn.close()
        return mensaje

def obtener_registros_usuarios():
    try:
        conn = pymysql.connect(**DATABASE_CONFIG)
        cur = conn.cursor()
        cur.execute(
            """
            SELECT * FROM usuario
            """
        )
        conn.commit()
    except BaseException as error:
        mensaje =  f"NO ANDA PORQUE {error}"
    finally:
        cur.close()
        conn.close()
        return True
    
def insertar_usuario(registro: dict, tipoUsuario = 2):
    try:
        conn = pymysql.connect(**DATABASE_CONFIG)
        cur = conn.cursor()
        cur.execute('INSERT INTO usuario (nombre, correo, contrasena, telefono, ciudad, direccion, idTipoUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (registro.get('nombre'), registro.get('correo'), registro.get('contraseña'), registro.get('telefono'), registro.get('ciudad'), registro.get('direccion'),tipoUsuario))
        conn.commit()
    except BaseException as error:
        mensaje =  f"NO ANDA PORQUE {error}"
    finally:
        cur.close()
        conn.close()

def verificar_usuario(correo, contraseña):
    usuario = []
    try:
        conn = pymysql.connect(**DATABASE_CONFIG)
        cur = conn.cursor()
        cur.execute('SELECT * FROM usuario WHERE correo = %s AND contrasena = %s', (correo, contraseña))
        usuario = cur.fetchone()
        cur.commit()
    except BaseException as error:
        mensaje =  f"NO ANDA PORQUE {error}"
    finally:
        cur.close()
        conn.close()
        return usuario
    
def seleccionar_codigo_admin():
    codigo = 0
    try:
        conn = pymysql.connect(**DATABASE_CONFIG)
        cur = conn.cursor()
        cur.execute(
            """
            SELECT * FROM codigo WHERE id = 1
            """
        )
        codigo = cur.fetchone()
        conn.commit()
    except BaseException as error:
        mensaje =  f"NO ANDA PORQUE {error}"
    finally:
        cur.close()
        conn.close()
        return codigo