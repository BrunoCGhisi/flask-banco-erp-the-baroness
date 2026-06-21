from database.connection import get_connection


def listar_hospedes():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            SELECT *
            FROM hospede
            ORDER BY id_hospede
        """)

        return cursor.fetchall()

    finally:

        cursor.close()
        conn.close()

def buscar_hospede_por_id(id_hospede):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            SELECT *
            FROM hospede
            WHERE id_hospede = %s
        """, (id_hospede,))

        return cursor.fetchone()

    finally:

        cursor.close()
        conn.close()

def criar_hospede(dados):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            INSERT INTO hospede(
                nome,
                cpf,
                telefone,
                email,
                endereco,
                data_nascimento
            )
            VALUES (%s,%s,%s,%s,%s,%s)
            RETURNING *
        """,
        (
            dados["nome"],
            dados["cpf"],
            dados["telefone"],
            dados["email"],
            dados["endereco"],
            dados["data_nascimento"]
        ))

        hospede = cursor.fetchone()

        conn.commit()

        return hospede

    finally:

        cursor.close()
        conn.close()

def atualizar_hospede(id_hospede, dados):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            UPDATE hospede
            SET
                nome = %s,
                telefone = %s,
                email = %s,
                endereco = %s,
                data_nascimento = %s
            WHERE id_hospede = %s
            RETURNING *
        """,
        (
            dados["nome"],
            dados["telefone"],
            dados["email"],
            dados["endereco"],
            dados["data_nascimento"],
            id_hospede
        ))

        hospede = cursor.fetchone()

        conn.commit()

        return hospede

    finally:

        cursor.close()
        conn.close()

def deletar_hospede(id_hospede):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            DELETE FROM hospede
            WHERE id_hospede = %s
        """, (id_hospede,))

        conn.commit()

    finally:

        cursor.close()
        conn.close()

