from flask import Blueprint

quartos_bp = Blueprint(
    "quartos",
    __name__,
    url_prefix="/quartos"
)

@quartos_bp.route("/", methods=["GET"])
def listar_quartos():
    return {
        "mensagem": "Lista de quartos"
    }