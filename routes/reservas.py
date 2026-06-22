from flask import Blueprint
from flask import jsonify
from flask import request

from services import reserva_service


reserva_bp = Blueprint(
    "reserva",
    __name__,
    url_prefix="/reservas"
)


@reserva_bp.route("/", methods=["GET"])
def listar():

    try:

        return jsonify(
            reserva_service.listar()
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 500


@reserva_bp.route("/", methods=["POST"])
def criar():

    try:

        dados = request.json

        return jsonify(
            reserva_service.criar(
                dados
            )
        ), 201

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400


@reserva_bp.route(
    "/<int:id_reserva>/checkin",
    methods=["PUT"]
)
def checkin(id_reserva):

    try:

        return jsonify(
            reserva_service.checkin(
                id_reserva
            )
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400


@reserva_bp.route(
    "/<int:id_reserva>/checkout",
    methods=["PUT"]
)
def checkout(id_reserva):

    try:

        return jsonify(
            reserva_service.checkout(
                id_reserva
            )
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400

@reserva_bp.route(
    "/<int:id_reserva>",
    methods=["PUT"]
)
def atualizar(id_reserva):

    try:

        dados = request.json

        return jsonify(
            reserva_service.atualizar(
                id_reserva,
                dados
            )
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400


@reserva_bp.route(
    "/<int:id_reserva>",
    methods=["DELETE"]
)
def deletar(id_reserva):

    try:

        reserva_service.deletar(
            id_reserva
        )

        return jsonify({
            "mensagem":
                "Reserva removida com sucesso"
        })

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400