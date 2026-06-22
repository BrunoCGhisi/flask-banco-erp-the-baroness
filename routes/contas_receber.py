from flask import Blueprint
from flask import jsonify

from services import conta_receber_service


conta_receber_bp = Blueprint(
    "conta_receber",
    __name__,
    url_prefix="/contas-receber"
)


@conta_receber_bp.route("/", methods=["GET"])
def listar():

    try:

        return jsonify(
            conta_receber_service.listar()
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 500


@conta_receber_bp.route(
    "/<int:id_conta>",
    methods=["GET"]
)
def buscar(id_conta):

    try:

        return jsonify(
            conta_receber_service.buscar_por_id(
                id_conta
            )
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 500