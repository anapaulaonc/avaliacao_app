import sqlite3
from sqlite3 import Error

class EstudanteDAO:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.execute('PRAGMA foreign_keys = 1')

    def insert_estudante(self, estudante):
        sql = ''' INSERT INTO Estudantes(email, matricula, curso, senha, e_administrador)
                  VALUES(?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, estudante)
        self.conn.commit()
        return cur.lastrowid

    def update_estudante(self, estudante, id):
        sql = ''' UPDATE Estudantes SET email = ?, matricula = ?, curso = ?, senha = ?, e_administrador = ? WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, (*estudante, id))
        self.conn.commit()

    def delete_estudante(self, id):
        sql = 'DELETE FROM Estudantes WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()

  
    def close(self):
        if self.conn:
            self.conn.close()