import sqlite3
from sqlite3 import Error
connection = sqlite3.connect('database.db')

class AvaliacaoDAO:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.execute('PRAGMA foreign_keys = 1')

    def insert_avaliacao(self, avaliacao):
        sql = ''' INSERT INTO Avaliacoes(estudante_id, turma_id, avaliacao)
                  VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, avaliacao)
        self.conn.commit()
        return cur.lastrowid

    def update_avaliacao(self, avaliacao, id):
        sql = ''' UPDATE Avaliacoes SET estudante_id = ?, turma_id = ?, avaliacao = ? WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, (*avaliacao, id))
        self.conn.commit()

    def delete_avaliacao(self, id):
        sql = 'DELETE FROM Avaliacoes WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
