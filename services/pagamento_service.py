from repositories import pagamento_repository

def listar():

    return pagamento_repository.listar_pagamentos()

def registrar(dados):

    return pagamento_repository.registrar_pagamento(
        dados
    )