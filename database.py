from app import app
from Models.cliente_model import db
from Models.venta_model import db
from Models.compras_model import db
from Models.nuevo_model import db

with app.app_context():
    db.create_all()