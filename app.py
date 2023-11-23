from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__, static_url_path='/static')

# Database connection configuration
db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Chinni@123",
    "host": "localhost",
    "port": "5432"
}

# Function to create a database connection
def create_db_connection():
    return psycopg2.connect(**db_config)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = create_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            return redirect(url_for('homepage'))
        else:
            return "Login failed."
    return render_template('login.html')

# Define other routes and views
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def lo1():
    return render_template('login.html')

@app.route('/collections')
def collections():
    return render_template('collect.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        conn = create_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        conn.commit()
        cursor.close()
        conn.close()
        return "Signup successful!"

    return render_template('signup.html')

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'GET':
        # Retrieve the current user (you need to implement user authentication)
        username = "current_username"  # Replace with actual authentication logic
        conn = create_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('edit_profile.html', user=user)

    elif request.method == 'POST':
        # Update the user's profile based on the submitted form data
        username = "current_username"  # Replace with actual authentication logic
        print(request.form)  # Print form data for debugging
        print(request.form['username'], request.form['password'], request.form['email'])  # Print specific values for debugging

        conn = create_db_connection()
        cursor = conn.cursor()

        # Print the SQL query for debugging
        sql_query = "UPDATE users SET username = %s, password = %s, email = %s WHERE username = %s"
        print(cursor.mogrify(sql_query, (request.form['username'], request.form['password'], request.form['email'], username)))

        try:
            cursor.execute(sql_query, (request.form['username'], request.form['password'], request.form['email'], username))
            conn.commit()  # Commit changes to the database
            print(cursor.statusmessage)  # Print SQL execution status
        except psycopg2.Error as e:
            print(f"PostgreSQL Error: {e}")
            conn.rollback()  # Rollback changes in case of an error
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()  # Rollback changes in case of an error
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('edit_profile'))



if __name__ == '__main__':
    app.run(debug=True)