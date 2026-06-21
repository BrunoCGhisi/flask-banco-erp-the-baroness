from database.connection import get_connection


def listar_categorias():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       SELECT *
                       FROM categoria_quarto
                       ORDER BY id_categoria
                       """)

        return cursor.fetchall()

    finally:

        cursor.close()
        conn.close()


def buscar_categoria_por_id(id_categoria):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       SELECT *
                       FROM categoria_quarto
                       WHERE id_categoria = %s
                       """, (id_categoria,))

        return cursor.fetchone()

    finally:

        cursor.close()
        conn.close()


def criar_categoria(dados):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       INSERT INTO categoria_quarto (
                           nome,
                           descricao,
                           capacidade,
                           valor_diaria
                       )
                       VALUES (%s,%s,%s,%s)
                           RETURNING *
                       """,
                       (
                           dados["nome"],
                           dados["descricao"],
                           dados["capacidade"],
                           dados["valor_diaria"]
                       ))

        categoria = cursor.fetchone()

        conn.commit()

        return categoria

    finally:

        cursor.close()
        conn.close()


def atualizar_categoria(
        id_categoria,
        dados
):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       UPDATE categoria_quarto
                       SET
                           nome = %s,
                           descricao = %s,
                           capacidade = %s,
                           valor_diaria = %s
                       WHERE id_categoria = %s
                           RETURNING *
                       """,
                       (
                           dados["nome"],
                           dados["descricao"],
                           dados["capacidade"],
                           dados["valor_diaria"],
                           id_categoria
                       ))

        categoria = cursor.fetchone()

        conn.commit()

        return categoria

    finally:

        cursor.close()
        conn.close()


def deletar_categoria(id_categoria):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
                       DELETE
                       FROM categoria_quarto
                       WHERE id_categoria = %s
                       """, (id_categoria,))

        conn.commit()

    finally:

        cursor.close()
        conn.close()