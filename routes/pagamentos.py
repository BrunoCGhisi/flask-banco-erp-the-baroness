from flask import Blueprint

pagamentos_bp = Blueprint(
    "pagamentos",
    __name__,
    url_prefix="/pagamentos"
)

@pagamentos_bp.route("/", methods=["GET"])
def listar_pagamentos():
    return {
        "mensagem": "Lista de pagamentos"
    }
