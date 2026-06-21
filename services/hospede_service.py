from repositories import hospede_repository


def listar():
    return hospede_repository.listar_hospedes()


def buscar_por_id(id_hospede):
    return hospede_repository.buscar_hospede_por_id(
        id_hospede
    )


def criar(dados):
    return hospede_repository.criar_hospede(
        dados
    )


def atualizar(id_hospede, dados):
    return hospede_repository.atualizar_hospede(
        id_hospede,
        dados
    )


def deletar(id_hospede):
    return hospede_repository.deletar_hospede(
        id_hospede
    )