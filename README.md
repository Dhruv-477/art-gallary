# Art Gallery Exhibition

A web application for showcasing art exhibitions and handling visitor bookings.

## Features

- Gallery showcase with featured artworks
- Artist profiles and information
- Event scheduling and details
- Visitor booking system with database storage

## Technology Stack

- **Frontend**: HTML5, CSS3
- **Backend**: Python Flask
- **Database**: MySQL

## Setup Instructions

### Prerequisites

- Python 3.7+
- MySQL Server
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd art-gallary
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up MySQL database:
   - Create a database named `art_gallery`
   - Create a table for bookings:
     ```sql
     CREATE TABLE bookings (
         id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(255) NOT NULL,
         email VARCHAR(255) NOT NULL,
         date DATE NOT NULL,
         guests INT NOT NULL,
         message TEXT,
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );
     ```

4. Update database configuration in `app.py` if needed (host, user, password)

### Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## File Structure

- `app.py` - Main Flask application
- `index.html` - Main gallery page
- `style.css` - Additional styling
- `requirements.txt` - Python dependencies
- Image files for artworks and artists

## License

MIT License - see LICENSE file for details