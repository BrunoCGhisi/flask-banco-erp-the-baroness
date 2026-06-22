from repositories import reserva_repository


def listar():
    return reserva_repository.listar_reservas()


def criar(dados):
    return reserva_repository.criar_reserva(
        dados
    )


def checkin(id_reserva):
    return reserva_repository.realizar_checkin(
        id_reserva
    )


def checkout(id_reserva):
    return reserva_repository.realizar_checkout(
        id_reserva
    )

def atualizar(
        id_reserva,
        dados
):
    return reserva_repository.atualizar_reserva(
        id_reserva,
        dados
    )

def deletar(id_reserva):

    return reserva_repository.deletar_reserva(
        id_reserva
    )