from repositories import conta_receber_repository



def listar():

    return conta_receber_repository.listar_contas()



def buscar_por_id(id_conta):

    return conta_receber_repository.buscar_conta(
        id_conta
    )