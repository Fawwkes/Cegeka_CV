

## Setup

**Clone the Repository**
```
git clone https://github.com/Fawwkes/Cegeka_CV.git
```

**Create and Activate a Virtual Environment**
```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
.venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate
```

**Install Dependencies**
```
pip install -r requirements.txt
```

## Running the Server

**Set the Flask App Environment Variable**
```
cd app
# On Windows
set FLASK_APP=app.py
# On macOS and Linux
export FLASK_APP=app.py
```

**Start the Flask Server**
```
flask run
```
The server by default starts at `http://127.0.0.1:5000/`.

**Accessing the Endpoints**
You can access the API endpoints through a browser or tools like curl or Postman. For example:
```
curl http://127.0.0.1:5000/personal
```

## Running Commands

**List Available Commands**
```
flask --help
```

**Execute a Specific Command**
```
flask <command-name> <argument>
```
For example:
```
flask export-cv experience
```

## Running Tests

**Execute Unit Tests**
```
python -m unittest
```
This command discovers and executes all tests written in the project.

**Test Output**
Observe the test results in the terminal. It will show which tests have passed and which have failed.

---
