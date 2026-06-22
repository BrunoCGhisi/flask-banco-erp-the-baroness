from database.connection import get_connection


def listar_quartos():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       SELECT
                           q.id_quarto,
                           q.numero,
                           q.andar,
                           q.status,
                           q.id_categoria,
                           c.nome AS categoria
                       FROM quarto q
                                JOIN categoria_quarto c
                                     ON c.id_categoria = q.id_categoria
                       ORDER BY q.id_quarto
                       """)

        return cursor.fetchall()

    finally:

        cursor.close()
        conn.close()


def buscar_quarto_por_id(id_quarto):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       SELECT *
                       FROM quarto
                       WHERE id_quarto = %s
                       """, (id_quarto,))

        return cursor.fetchone()

    finally:

        cursor.close()
        conn.close()


def criar_quarto(dados):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       INSERT INTO quarto(
                           numero,
                           andar,
                           status,
                           id_categoria
                       )
                       VALUES (%s,%s,%s,%s)
                           RETURNING *
                       """,
                       (
                           dados["numero"],
                           dados["andar"],
                           dados["status"],
                           dados["id_categoria"]
                       ))

        quarto = cursor.fetchone()

        conn.commit()

        return quarto

    finally:

        cursor.close()
        conn.close()


def atualizar_quarto(id_quarto, dados):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       UPDATE quarto
                       SET
                           numero = %s,
                           andar = %s,
                           status = %s,
                           id_categoria = %s
                       WHERE id_quarto = %s
                           RETURNING *
                       """,
                       (
                           dados["numero"],
                           dados["andar"],
                           dados["status"],
                           dados["id_categoria"],
                           id_quarto
                       ))

        quarto = cursor.fetchone()

        conn.commit()

        return quarto

    finally:

        cursor.close()
        conn.close()


def deletar_quarto(id_quarto):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       DELETE FROM quarto
                       WHERE id_quarto = %s
                       """, (id_quarto,))

        conn.commit()

    finally:

        cursor.close()
        conn.close()