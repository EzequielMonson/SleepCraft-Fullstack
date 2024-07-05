from flask import Flask, render_template
from flask_cors import CORS
from app.views import *

app = Flask(__name__)
app.secret_key = '4b89ac97746a5998ab553a96294d571513d09f505ac50ad3'
CORS(app)
app.route('/', methods=['GET'])(index)
app.route('/index', methods=['GET'])(index)
app.route('/traer_datos', methods=['GET'])(traer_datos)
# Ruta para mostrar el formulario
app.route('/login', methods=['GET'])(mostrar_login)
app.route('/login', methods=['POST'])(loguear_usuario)
app.route('/codigo', methods=['GET'])(buscar_codigo_admin)
app.route('/registrar', methods=['POST', 'GET'])(registrar_usuario)
app.route('/logout', methods=['GET'])(logout)
app.route('/guardarCorreo', methods=['GET'])(traer_correo)
app.route('/contacto', methods=['GET'])(contacto)
app.route('/productos', methods=['GET'])(productos)
app.route('/compras', methods=['GET'])(compras)
app.route('/integrantes', methods=['GET'])(integrantes)
if __name__ == '__main__':
    app.run(debug=True)
    