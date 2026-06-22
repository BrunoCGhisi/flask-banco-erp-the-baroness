from flask import Blueprint
from flask import request
from flask import jsonify

from services import quarto_service


quarto_bp = Blueprint(
    "quarto",
    __name__,
    url_prefix="/quartos"
)


@quarto_bp.route("/", methods=["GET"])
def listar():

    try:

        return jsonify(
            quarto_service.listar()
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 500


@quarto_bp.route("/<int:id_quarto>", methods=["GET"])
def buscar(id_quarto):

    try:

        return jsonify(
            quarto_service.buscar_por_id(
                id_quarto
            )
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 500


@quarto_bp.route("/", methods=["POST"])
def criar():

    try:

        dados = request.json

        quarto = quarto_service.criar(
            dados
        )

        return jsonify(
            quarto
        ), 201

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400


@quarto_bp.route("/<int:id_quarto>", methods=["PUT"])
def atualizar(id_quarto):

    try:

        dados = request.json

        quarto = quarto_service.atualizar(
            id_quarto,
            dados
        )

        return jsonify(
            quarto
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400


@quarto_bp.route("/<int:id_quarto>", methods=["DELETE"])
def deletar(id_quarto):

    try:

        quarto_service.deletar(
            id_quarto
        )

        return jsonify({
            "mensagem":
                "Quarto removido com sucesso"
        })

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400