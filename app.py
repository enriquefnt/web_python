from flask import Flask, request, render_template
import mariadb
import json

app = Flask(__name__)
app.config["DEBUG"] = True


# Configuración de conexión a MariaDB
config = {
    'host': 'mariadb',
    'port': 3306,
    'user': 'root',
    'password': 'Password123!',
    'database': 'demo'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_person():
    name = request.form['name']
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("INSERT INTO people (name) VALUES (?)", (name,))
    conn.commit()
    return "Persona añadida"

@app.route('/api/people', methods=['GET'])
def get_people():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM people")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json.dumps(json_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
