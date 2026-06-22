from database.connection import get_connection


def listar_reservas():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       SELECT *
                       FROM vw_reservas_ativas
                       ORDER BY id_reserva
                       """)

        return cursor.fetchall()

    finally:

        cursor.close()
        conn.close()


def criar_reserva(dados):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            CALL sp_criar_reserva(
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """,
                       (
                           dados["id_hospede_responsavel"],
                           dados["id_quarto"],
                           dados["checkin_previsto"],
                           dados["checkout_previsto"],
                           dados["quantidade_hospedes"]
                       ))

        conn.commit()

        return {
            "mensagem":
                "Reserva criada com sucesso"
        }

    finally:

        cursor.close()
        conn.close()


def realizar_checkin(id_reserva):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            CALL sp_realizar_checkin(%s)
        """, (id_reserva,))

        conn.commit()

        return {
            "mensagem":
                "Check-in realizado"
        }

    finally:

        cursor.close()
        conn.close()


def realizar_checkout(id_reserva):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            CALL sp_realizar_checkout(%s)
        """, (id_reserva,))

        conn.commit()

        return {
            "mensagem":
                "Checkout realizado"
        }

    finally:

        cursor.close()
        conn.close()