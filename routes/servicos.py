from flask import (
    Blueprint,
    request,
    jsonify
)

from services import servico_service


servico_bp = Blueprint(
    "servico",
    __name__,
    url_prefix="/servicos"
)


@servico_bp.route("/", methods=["GET"])
def listar():

    try:

        return jsonify(
            servico_service.listar()
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 500


@servico_bp.route(
    "/<int:id_servico>",
    methods=["GET"]
)
def buscar(id_servico):

    try:

        return jsonify(
            servico_service.buscar_por_id(
                id_servico
            )
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 500


@servico_bp.route("/", methods=["POST"])
def criar():

    try:

        dados = request.json

        servico = servico_service.criar(
            dados
        )

        return jsonify(
            servico
        ), 201

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400


@servico_bp.route(
    "/<int:id_servico>",
    methods=["PUT"]
)
def atualizar(id_servico):

    try:

        dados = request.json

        servico = servico_service.atualizar(
            id_servico,
            dados
        )

        return jsonify(
            servico
        )

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400


@servico_bp.route(
    "/<int:id_servico>",
    methods=["DELETE"]
)
def deletar(id_servico):

    try:

        servico_service.deletar(
            id_servico
        )

        return jsonify({
            "mensagem":
                "Serviço removido com sucesso"
        })

    except Exception as e:

        return jsonify({
            "erro": str(e)
        }), 400