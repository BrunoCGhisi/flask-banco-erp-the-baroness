from database.connection import get_connection


def listar_pagamentos():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       SELECT *
                       FROM pagamento
                       ORDER BY id_pagamento
                       """)

        return cursor.fetchall()

    finally:

        cursor.close()
        conn.close()


def registrar_pagamento(dados):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            CALL sp_registrar_pagamento(
                %s,
                %s,
                %s
            )
        """,
                       (
                           dados["id_conta"],
                           dados["valor"],
                           dados["id_forma_pagamento"]
                       ))

        conn.commit()

        return {
            "mensagem":
                "Pagamento registrado com sucesso"
        }

    finally:

        cursor.close()
        conn.close()