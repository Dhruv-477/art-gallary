import cgi
import cgitb
import os
import sys

# Enable CGI error reporting
cgitb.enable()

def main():
    # Set content type for HTTP response
    print("Content-Type: text/html\n")
    
    # Database connection parameters
    servername = "localhost"
    username = "root"
    password = ""
    dbname = "art_gallery"
    
    try:
        # Try to import mysql connector (preferred method)
        try:
            import mysql.connector
            from mysql.connector import Error
            
            # Create database connection
            conn = mysql.connector.connect(
                host=servername,
                user=username,
                password=password,
                database=dbname
            )
            
            if conn.is_connected():
                cursor = conn.cursor()
                
                # Get form data
                form = cgi.FieldStorage()
                
                # Check if this is a POST request
                if os.environ.get('REQUEST_METHOD') == 'POST':
                    # Extract form fields
                    name = form.getvalue('name', '').strip()
                    email = form.getvalue('email', '').strip()
                    date = form.getvalue('date', '')
                    guests = int(form.getvalue('guests', 0))
                    message = form.getvalue('message', '').strip()
                    
                    # Prepare and execute SQL statement
                    query = "INSERT INTO bookings (name, email, date, guests, message) VALUES (%s, %s, %s, %s, %s)"
                    values = (name, email, date, guests, message)
                    
                    cursor.execute(query, values)
                    conn.commit()
                    
                    print("Booking submitted successfully!")
                
                # Close database connection
                cursor.close()
                conn.close()
        
        except ImportError:
            # Fallback to pymysql if mysql.connector is not available
            try:
                import pymysql
                
                # Create database connection
                conn = pymysql.connect(
                    host=servername,
                    user=username,
                    password=password,
                    database=dbname,
                    charset='utf8mb4'
                )
                
                with conn.cursor() as cursor:
                    # Get form data
                    form = cgi.FieldStorage()
                    
                    # Check if this is a POST request
                    if os.environ.get('REQUEST_METHOD') == 'POST':
                        # Extract form fields
                        name = form.getvalue('name', '').strip()
                        email = form.getvalue('email', '').strip()
                        date = form.getvalue('date', '')
                        guests = int(form.getvalue('guests', 0))
                        message = form.getvalue('message', '').strip()
                        
                        # Prepare and execute SQL statement
                        query = "INSERT INTO bookings (name, email, date, guests, message) VALUES (%s, %s, %s, %s, %s)"
                        values = (name, email, date, guests, message)
                        
                        cursor.execute(query, values)
                        conn.commit()
                        
                        print("Booking submitted successfully!")
                
                conn.close()
                
            except ImportError:
                print("Error: MySQL connector not available. Please install mysql-connector-python or pymysql.")
                print("Run: pip install mysql-connector-python")
                sys.exit(1)
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
