from repositories import quarto_repository


def listar():
    return quarto_repository.listar_quartos()


def buscar_por_id(id_quarto):
    return quarto_repository.buscar_quarto_por_id(
        id_quarto
    )


def criar(dados):
    return quarto_repository.criar_quarto(
        dados
    )


def atualizar(id_quarto, dados):
    return quarto_repository.atualizar_quarto(
        id_quarto,
        dados
    )


def deletar(id_quarto):
    quarto_repository.deletar_quarto(
        id_quarto
    )