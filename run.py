from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://emofit.netlify.app"}})

# Your routes here

if __name__ == '__main__':
    app.run()