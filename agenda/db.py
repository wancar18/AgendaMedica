import sqlite3

DB_NAME = "consultas.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabelas():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS medicos (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS consultas (
                id INTEGER PRIMARY KEY,
                paciente TEXT NOT NULL,
                medico_id INTEGER,
                data TEXT,
                hora TEXT,
                FOREIGN KEY (medico_id) REFERENCES medicos(id)
            )
        """)
        conn.commit()

def cadastrar_medicos():
    medicos = ["Dr. Ana", "Dr. Bruno", "Dr. Carlos", "Dr. Daniela", "Dr. Eduardo"]
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT OR IGNORE INTO medicos (id, nome) VALUES (?, ?)",
                           [(i+1, nome) for i, nome in enumerate(medicos)])
        conn.commit()

def agendar_consulta(paciente, medico_id, data, hora):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM consultas WHERE medico_id = ? AND data = ? AND hora = ?",
                       (medico_id, data, hora))
        if cursor.fetchone():
            return False
        cursor.execute("INSERT INTO consultas (paciente, medico_id, data, hora) VALUES (?, ?, ?, ?)",
                       (paciente, medico_id, data, hora))
        conn.commit()
        return True

def listar_consultas(medico_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT consultas.id, paciente, data, hora FROM consultas
            WHERE medico_id = ? ORDER BY data, hora
        """, (medico_id,))
        return cursor.fetchall()

def alterar_consulta(consulta_id, nova_data, nova_hora):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT medico_id FROM consultas WHERE id = ?", (consulta_id,))
        resultado = cursor.fetchone()
        if not resultado:
            return False
        medico_id = resultado[0]
        cursor.execute("SELECT * FROM consultas WHERE medico_id = ? AND data = ? AND hora = ?",
                       (medico_id, nova_data, nova_hora))
        if cursor.fetchone():
            return False
        cursor.execute("UPDATE consultas SET data = ?, hora = ? WHERE id = ?",
                       (nova_data, nova_hora, consulta_id))
        conn.commit()
        return True

def cancelar_consulta(consulta_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM consultas WHERE id = ?", (consulta_id,))
        conn.commit()
