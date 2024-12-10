from flask import flask  # type: ignore

from flask import Flask
from Controllers.inicio_controllers import inicio_blueprint
from Controllers.cliente_controllers import cliente_blueprint
from Controllers.venta_controllers import venta_blueprint
from Controllers.compras_controllers import compras_blueprint
from Controllers.nuevo_controllers import nuevo_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'

# Registro de Blueprints
app.register_blueprint(inicio_blueprint)
app.register_blueprint(cliente_blueprint)
app.register_blueprint(venta_blueprint)
app.register_blueprint(compras_blueprint)
app.register_blueprint(nuevo_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
    
