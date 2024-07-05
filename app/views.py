from flask import jsonify, request, render_template, redirect, url_for,session
from app.database import *
from app.models import *
def index():
    # crear_tablas()
    return render_template('index.html')
def contacto ():
    return render_template('contacto.html')
def productos ():
    return render_template('productos.html')
def integrantes():
    return render_template('integrantes.html')
def compras():
    return render_template('compras.html')
def traer_datos():
    return jsonify(session.get('datosusuario'))
def registrar_usuario():
    if request.method == 'POST':
        #print("Formulario recibido:", request.form)
        # Guardar la información del usuario en la base de datos
        if request.form.get('tipoUsuario') == 'true':
            administradorActual = Administrador(request.form)
            session['datosusuario'] = administradorActual.to_dict()
            insertar_usuario(request.form, 1)
        else:
            cliente_actual = Cliente(request.form)
            session['datosusuario'] = cliente_actual.to_dict()
            insertar_usuario(request.form)
        return redirect(url_for('index'))
    else:
        return render_template('registrarse.html')
    
def loguear_usuario():
    if request.method == 'POST':
        correo = request.form.get('correo')
        contrasena = request.form.get('contraseña')
        print(request.form.get('contraseña'))
        usuario_encontrado = verificar_usuario(correo, contrasena)
        print(type(request.form))
        if usuario_encontrado:
            if usuario_encontrado[7] == 2:
                cliente_actual = Cliente((usuario_encontrado))
                session['datosusuario'] = cliente_actual.to_dict()
                print(session)
            elif usuario_encontrado[7] == 1:
                adminstrador_actual = Administrador(request.form)
                session['datosusuario'] = adminstrador_actual.to_dict()
            return redirect(url_for('index'))
        else:
            print('contraseña o usuario no validos')
            return render_template('iniciarSesion.html', error='Correo o contraseña incorrectos')

    return render_template('iniciarSesion.html')

def mostrar_login():
    return render_template('iniciarSesion.html')

def buscar_codigo_admin():
    codigoAdmin = seleccionar_codigo_admin()
    return jsonify({'codigo' : f'{codigoAdmin[1]}'})

def traer_correo():
        correo = session.get('correo', '')
        return jsonify({'correo': correo})


def logout():
    # Cerrar sesión y redireccionar al usuario a la página de inicio de sesión
    session.clear()
    return redirect(url_for('index'))