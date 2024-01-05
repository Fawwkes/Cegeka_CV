from flask import Flask
from routes import api  # Ensure this path is correct
from commands import register_commands

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(api)
register_commands(app)

# You can define CLI commands here

if __name__ == '__main__':
    app.run(debug=True)
