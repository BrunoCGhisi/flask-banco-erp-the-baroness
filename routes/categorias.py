from flask import (
    Blueprint,
    jsonify,
    request
)

from services import categoria_service

categoria_bp = Blueprint(
    "categoria",
    __name__,
    url_prefix="/categorias"
)


@categoria_bp.route("/", methods=["GET"])
def listar():

    return jsonify(
        categoria_service.listar()
    )


@categoria_bp.route(
    "/<int:id_categoria>",
    methods=["GET"]
)
def buscar(id_categoria):

    return jsonify(
        categoria_service.buscar_por_id(
            id_categoria
        )
    )


@categoria_bp.route("/", methods=["POST"])
def criar():

    dados = request.json

    categoria = categoria_service.criar(
        dados
    )

    return jsonify(categoria), 201


@categoria_bp.route(
    "/<int:id_categoria>",
    methods=["PUT"]
)
def atualizar(id_categoria):

    dados = request.json

    categoria = categoria_service.atualizar(
        id_categoria,
        dados
    )

    return jsonify(categoria)


@categoria_bp.route(
    "/<int:id_categoria>",
    methods=["DELETE"]
)
def deletar(id_categoria):

    categoria_service.deletar(
        id_categoria
    )

    return jsonify({
        "mensagem":
            "Categoria removida com sucesso"
    })