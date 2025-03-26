from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from models import db, User, Pianeta  
import os

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/sofiatronci/Downloads/flask/db/planetario.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'la-tua-chiave-segreta'

# Initialize the database with the app
db.init_app(app)

@app.route("/pianeti")
def pianeti():
    # Recupera tutti i pianeti ordinati per id
    lista_pianeti = Pianeta.query.order_by(Pianeta.id).all()
    return render_template("pianeta.html", pianeti=lista_pianeti)

# Route per la homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Route per il login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(email=email, username=username).first()
        if user and user.password == password:  # Direct password comparison
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login effettuato con successo!', 'success')
            return redirect(url_for('personale'))
        else:
            flash('Credenziali non valide', 'danger')
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()  # Clear all session data
    return redirect(url_for('homepage')) 


# Route per la registrazione
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        if User.query.filter((User.email == email) | (User.username == username)).first():
            flash('Email o Username già esistenti!', 'danger')
            return redirect(url_for('register'))
        
        new_user = User(email=email, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registrazione avvenuta con successo! Ora effettua il login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Area personale (accessibile solo se loggati)
@app.route('/personale')
def personale():
    if 'user_id' not in session:
        flash('Effettua il login per accedere all\'area personale', 'warning')
        return redirect(url_for('login'))
    return render_template('personale.html', username=session.get('username'))

planet_names = {
    "mercurio": 1,
    "venere": 2,
    "terra": 3,
    "marte": 4,
    "giove": 5,
    "saturno": 6,
    "urano": 7,
    "nettuno": 8
}
@app.route('/pianeta/<nome>')
def pianeta(nome):
    planet_id = planet_names.get(nome.lower())
    if planet_id is None:
        abort(404)

    # Using ilike for a case-insensitive match
    planet = Pianeta.query.filter(Pianeta.nome.ilike(nome)).first()
    if not planet:
        abort(404)
    return render_template('pianeta.html', current_planet=planet)


if __name__ == '__main__':
    # Per la prima esecuzione, crea il database all'interno del contesto dell'applicazione
    os.makedirs('/Users/sofiatronci/Downloads/flask/db', exist_ok=True)
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database created successfully.")
    app.run(debug=True)