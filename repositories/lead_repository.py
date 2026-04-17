from database import get_connection


def get_all_leads():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, email, interesse, valor, created_at
        FROM leads
        ORDER BY id DESC
    """)

    leads = cursor.fetchall()
    conn.close()
    return leads


def get_lead_by_id(lead_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, email, interesse, valor, created_at
        FROM leads
        WHERE id = ?
    """, (lead_id,))

    lead = cursor.fetchone()
    conn.close()
    return lead


def create_lead(nome, email, interesse, valor):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO leads (nome, email, interesse, valor)
        VALUES (?, ?, ?, ?)
    """, (nome, email, interesse, valor))

    lead_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return lead_id


def update_lead(lead_id, nome, email, interesse, valor):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE leads
        SET nome = ?, email = ?, interesse = ?, valor = ?
        WHERE id = ?
    """, (nome, email, interesse, valor, lead_id))

    conn.commit()
    conn.close()


def delete_lead(lead_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM leads WHERE id = ?", (lead_id,))

    conn.commit()
    conn.close()