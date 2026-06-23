from flask import (
    Blueprint,
    jsonify,
    request
)

from services import pagamento_service

pagamento_bp = Blueprint(
    "pagamento",
    __name__,
    url_prefix="/pagamentos"
)

@pagamento_bp.route("/", methods=["GET"])
def listar():

    try:

        return jsonify(
            pagamento_service.listar()
        )

    except Exception as e:

        return jsonify({
            "erro":str(e)
        }),500

@pagamento_bp.route("/", methods=["POST"])
def registrar():

    try:

        dados = request.json
        return jsonify(
            pagamento_service.registrar(
                dados
            )
        ),201

    except Exception as e:

        return jsonify({
            "erro":str(e)
        }),400