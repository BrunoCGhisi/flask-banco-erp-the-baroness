from flask import Flask
from flask_cors import CORS

from routes.quartos import quartos_bp
from routes.hospedes import hospede_bp
from routes.reservas import reservas_bp
from routes.pagamentos import pagamentos_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(quartos_bp)
app.register_blueprint(hospede_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(pagamentos_bp)

@app.route("/")
def home():
    return {
        "mensagem": "API Hotel funcionando"
    }

if __name__ == "__main__":
    app.run(debug=True)