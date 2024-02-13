import mysql.connector
from os import getenv, path
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, jsonify)

app = Flask(__name__)

def connect_to_db():
    app.config['MYSQL_HOST'] = getenv('DB_HOST')
    app.config['MYSQL_DB'] = getenv('DB_DATABASE')
    app.config['MYSQL_USER'] = getenv('DB_USERNAME')
    app.config['MYSQL_PASSWORD'] = getenv('DB_PASSWORD')
    cnx = mysql.connector.connect(user=getenv('DB_USERNAME'), password=getenv('DB_PASSWORD'),
                                host=getenv('DB_HOST'),
                                database=getenv('DB_DATABASE'),
                                connection_timeout=6)
    return cnx

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))
   
@app.route("/get")
def get():
    try: 
        cnx = connect_to_db()
        query = ("SELECT FirstName, LastName FROM Persons WHERE PersonID = 1;")
        cursor = cnx.cursor()
        cursor.execute(query)
        name, lastname = cursor.fetchone()
        user_data = {
            "name": name,
            "lastname": lastname
        }
        return jsonify(user_data)
    except:
        response = {
            "Error": f"Error when connecting to database {app.config['MYSQL_HOST']}"
        }
    return jsonify(response)

if __name__ == '__main__':
   app.run()
