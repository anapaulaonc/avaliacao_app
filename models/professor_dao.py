import sqlite3
from sqlite3 import Error

connection = sqlite3.connect('database.db')
cur = connection.cursor()

class ProfessorDAO:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.execute('PRAGMA foreign_keys = 1')

    def insert_professor(self, professor):
        sql = ''' INSERT INTO Professores(nome, departamento_id)
                  VALUES(?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, professor)
        self.conn.commit()
        return cur.lastrowid

    def update_professor(self, professor, id):
        sql = ''' UPDATE Professores SET nome = ?, departamento_id = ? WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, (*professor, id))
        self.conn.commit()

    def delete_professor(self, id):
        sql = 'DELETE FROM Professores WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()




