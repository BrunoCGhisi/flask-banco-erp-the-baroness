from flask import Flask
from flask_cors import CORS

from routes.hospedes import hospede_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(hospede_bp)

@app.route("/")
def home():
    return {
        "mensagem": "Barones Hotel API"
    }

if __name__ == "__main__":
    app.run(debug=True)