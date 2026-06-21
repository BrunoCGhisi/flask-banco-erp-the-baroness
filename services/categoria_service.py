from repositories import categoria_repository


def listar():
    return categoria_repository.listar_categorias()


def buscar_por_id(id_categoria):
    return categoria_repository.buscar_categoria_por_id(
        id_categoria
    )


def criar(dados):
    return categoria_repository.criar_categoria(
        dados
    )


def atualizar(id_categoria, dados):
    return categoria_repository.atualizar_categoria(
        id_categoria,
        dados
    )


def deletar(id_categoria):
    return categoria_repository.deletar_categoria(
        id_categoria
    )