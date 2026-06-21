from flask import Blueprint

hospedes_bp = Blueprint(
    "hospedes",
    __name__,
    url_prefix="/hospedes"
)

@hospedes_bp.route("/", methods=["GET"])
def listar_hospedes():
    return {
        "mensagem": "Lista de hóspedes"
    }