from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import qrcode

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@db/mydatabase'
db = SQLAlchemy(app)

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        name = request.form['name']
        new_url = Url(url=url, name=name)
        db.session.add(new_url)
        db.session.commit()
        qr = qrcode.make(url)
        # ... Guardar el código QR como imagen
    return render_template('index.html')

@app.route('/get_qr_code')
def get_qr_code():
    # Obtener la última URL guardada en la base de datos
    last_url = Url.query.order_by(Url.id.desc()).first()
    qr = qrcode.make(last_url.url)
    # Guardar la imagen del código QR en un directorio estático
    qr.save('static/qr_code.png')
    return jsonify({'qr_code_url': '/static/qr_code.png'})