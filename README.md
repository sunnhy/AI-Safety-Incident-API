# HumanChain AI Safety Incident Log API
 A simple Flask + MongoDB REST API to log and manage AI safety incidents.

# Features of the API
- Log new incidents with title, description, and severity
- View all logged incidents
- Fetch individual incidents by ID
- Delete incidents by ID
- Input validation for required fields and severity levels

# Tech stack
- Python 3.13.2
- Flask 2.3.2
- MongoDB
- PyMongo (MongoDB driver)
- dotenv (for environment variable management)

# Setup
1. Create a virtual environment and activate it:
        python -m venv venv
        venv\Scripts\activate  # On Windows

2. Install dependencies:
        pip install -r requirements.txt

3. Start MongoDB locally.

4. Insert sample data:
        python sample_data.py

5. Run the Flask server:
        python app.py