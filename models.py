from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modello per gli utenti
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Modello per la tabella pianeti
class Pianeta(db.Model):
    __tablename__ = 'pianeti'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    eta = db.Column(db.Integer, nullable=False)
    dimensioni = db.Column(db.Integer, nullable=False)
    composizione = db.Column(db.String, nullable=False)
    dist = db.Column(db.Integer, nullable=False)
    distT = db.Column(db.Integer, nullable=False)
    lenY = db.Column(db.Integer, nullable=False)