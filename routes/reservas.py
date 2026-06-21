from flask import Blueprint

reservas_bp = Blueprint(
    "reservas",
    __name__,
    url_prefix="/reservas"
)

@reservas_bp.route("/", methods=["GET"])
def listar_reservas():
    return {
        "mensagem": "Lista de reservas"
    }