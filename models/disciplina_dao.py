import sqlite3
from sqlite3 import Error


class DisciplinaDAO:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.execute('PRAGMA foreign_keys = 1')

    def insert_disciplina(self, disciplina):
        sql = ''' INSERT INTO Disciplinas(nome, departamento_id)
                  VALUES(?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, disciplina)
        self.conn.commit()
        return cur.lastrowid

    def update_disciplina(self, disciplina, id):
        sql = ''' UPDATE Disciplinas SET nome = ?, departamento_id = ? WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, (*disciplina, id))
        self.conn.commit()

    def delete_disciplina(self, id):
        sql = 'DELETE FROM Disciplinas WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
