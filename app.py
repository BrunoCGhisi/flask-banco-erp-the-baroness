from flask import Flask
from flask_cors import CORS

from routes.hospedes import hospede_bp
from routes.categorias import categoria_bp
from routes.quartos import quarto_bp
from routes.reservas import reserva_bp
from routes.contas_receber import conta_receber_bp
from routes.pagamentos import pagamento_bp
from routes.servicos import servico_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(hospede_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(quarto_bp)
app.register_blueprint(reserva_bp)
app.register_blueprint(conta_receber_bp)
app.register_blueprint(pagamento_bp)
app.register_blueprint(servico_bp)


@app.route("/")
def home():
    return {
        "mensagem": "Barones Hotel API"
    }

if __name__ == "__main__":
    app.run(debug=True)