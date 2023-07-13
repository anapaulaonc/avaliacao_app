import sqlite3
from sqlite3 import Error

class TurmaDAO:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.execute('PRAGMA foreign_keys = 1')

    def insert_turma(self, turma):
        sql = ''' INSERT INTO Turmas(disciplina_id, professor_id)
                  VALUES(?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, turma)
        self.conn.commit()
        return cur.lastrowid

    def update_turma(self, turma, id):
        sql = ''' UPDATE Turmas SET disciplina_id = ?, professor_id = ? WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, (*turma, id))
        self.conn.commit()

    def delete_turma(self, id):
        sql = 'DELETE FROM Turmas WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()

