from database.connection import get_connection


def listar_servicos():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       SELECT *
                       FROM servico
                       ORDER BY id_servico
                       """)

        return cursor.fetchall()

    finally:

        cursor.close()
        conn.close()


def buscar_servico_por_id(id_servico):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       SELECT *
                       FROM servico
                       WHERE id_servico = %s
                       """, (id_servico,))

        return cursor.fetchone()

    finally:

        cursor.close()
        conn.close()


def criar_servico(dados):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       INSERT INTO servico(
                           nome,
                           valor
                       )
                       VALUES (%s, %s)
                           RETURNING *
                       """,
                       (
                           dados["nome"],
                           dados["valor"]
                       ))

        servico = cursor.fetchone()

        conn.commit()

        return servico

    finally:

        cursor.close()
        conn.close()


def atualizar_servico(
        id_servico,
        dados
):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       UPDATE servico
                       SET
                           nome = %s,
                           valor = %s
                       WHERE id_servico = %s
                           RETURNING *
                       """,
                       (
                           dados["nome"],
                           dados["valor"],
                           id_servico
                       ))

        servico = cursor.fetchone()

        conn.commit()

        return servico

    finally:

        cursor.close()
        conn.close()


def deletar_servico(id_servico):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       DELETE
                       FROM servico
                       WHERE id_servico = %s
                       """, (id_servico,))

        conn.commit()

    finally:

        cursor.close()
        conn.close()