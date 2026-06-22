from repositories import servico_repository


def listar():
    return servico_repository.listar_servicos()


def buscar_por_id(id_servico):
    return servico_repository.buscar_servico_por_id(
        id_servico
    )


def criar(dados):
    return servico_repository.criar_servico(
        dados
    )


def atualizar(id_servico, dados):
    return servico_repository.atualizar_servico(
        id_servico,
        dados
    )


def deletar(id_servico):
    servico_repository.deletar_servico(
        id_servico
    )