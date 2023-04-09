  
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Connectia@143'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        firstname = userDetails['firstname']
        lastname = userDetails['lastname']
        email = userDetails['email']
        phone = userDetails['phone']
        dob = userDetails['dob']
        gender = userDetails['gender']
        address1 = userDetails['address1']
        address2 = userDetails['address2']
        city = userDetails['city']
        state = userDetails['state']
        zipcode = userDetails['zipcode']
        country = userDetails['country']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students(first_name, last_name, email, mobile_no, dob, gender, address1, address2, city, state, zip_code, country) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(firstname, lastname, email, phone, dob, gender, address1, address2, city, state, zipcode, country))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')


@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM students")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)