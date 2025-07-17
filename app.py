from flask import Flask, request, render_template_string, redirect, url_for
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'art_gallery'
}

def get_db_connection():
    """Create and return a database connection."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def index():
    """Serve the main gallery page."""
    try:
        with open('index.html', 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Gallery page not found", 404

@app.route('/register', methods=['POST'])
def register():
    """Handle booking form submissions."""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        date = request.form.get('date', '')
        guests = request.form.get('guests', 0)
        message = request.form.get('message', '').strip()
        
        # Validate required fields
        if not all([name, email, date, guests]):
            return "All required fields must be filled", 400
        
        try:
            guests = int(guests)
        except ValueError:
            return "Invalid number of guests", 400
        
        # Database operation
        connection = get_db_connection()
        if connection is None:
            return "Database connection failed", 500
        
        try:
            cursor = connection.cursor()
            
            # Insert booking data
            query = "INSERT INTO bookings (name, email, date, guests, message) VALUES (%s, %s, %s, %s, %s)"
            values = (name, email, date, guests, message)
            
            cursor.execute(query, values)
            connection.commit()
            
            return "Booking submitted successfully!"
            
        except Error as e:
            print(f"Database error: {e}")
            return f"Error: {e}", 500
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)