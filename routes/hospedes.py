from flask import Blueprint, request, jsonify

from services import hospede_service

hospede_bp = Blueprint(
    "hospede",
    __name__,
    url_prefix="/hospedes"
)


@hospede_bp.route("/", methods=["GET"])
def listar():

    try:

        return jsonify(
            hospede_service.listar()
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 500


@hospede_bp.route("/<int:id_hospede>", methods=["GET"])
def buscar(id_hospede):

    try:

        return jsonify(
            hospede_service.buscar_por_id(
                id_hospede
            )
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 500


@hospede_bp.route("/", methods=["POST"])
def criar():

    try:

        dados = request.json

        hospede = hospede_service.criar(
            dados
        )

        return jsonify(
            hospede
        ), 201

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400


@hospede_bp.route("/<int:id_hospede>", methods=["PUT"])
def atualizar(id_hospede):

    try:

        dados = request.json

        hospede = hospede_service.atualizar(
            id_hospede,
            dados
        )

        return jsonify(
            hospede
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400


@hospede_bp.route("/<int:id_hospede>", methods=["DELETE"])
def deletar(id_hospede):

    try:

        hospede_service.deletar(
            id_hospede
        )

        return jsonify({
            "mensagem":
                "Hospede removido com sucesso"
        })

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400