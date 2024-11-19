from flask import Flask, render_template, request,flash,url_for,redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = PASS
app.config['MYSQL_DB'] = 'vastra'

mysql = MySQL(app)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/signin')
def signinpage():
    return render_template('signin.html')

@app.route('/submit', methods=['POST'])
def feedback():
    rating = request.form['rating']
    leave_ds = request.form['leave_ds']
    feed = request.form['feed']
    
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO feedback (rating, leave_des, feed) VALUES (%s, %s, %s)''', (rating, leave_ds, feed))
    mysql.connection.commit()
    cursor.close()
    flash('Feedback submitted successfully!', 'success')
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True)
