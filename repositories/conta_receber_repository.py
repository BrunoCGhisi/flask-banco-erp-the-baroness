from database.connection import get_connection


def listar_contas():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       SELECT *
                       FROM vw_situacao_financeira
                       ORDER BY id_reserva
                       """)

        return cursor.fetchall()

    finally:

        cursor.close()
        conn.close()


def buscar_conta(id_conta):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       SELECT *
                       FROM conta_receber
                       WHERE id_conta = %s
                       """, (id_conta,))

        return cursor.fetchone()

    finally:

        cursor.close()
        conn.close()