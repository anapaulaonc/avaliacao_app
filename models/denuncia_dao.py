import sqlite3
from sqlite3 import Error

class DenunciaDAO:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.execute('PRAGMA foreign_keys = 1')

    def insert_denuncia(self, denuncia):
        sql = ''' INSERT INTO Denuncias(avaliacao_id, estudante_id, administrador_id, denuncia)
                  VALUES(?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, denuncia)
        self.conn.commit()
        return cur.lastrowid

    def update_denuncia(self, denuncia, id):
        sql = ''' UPDATE Denuncias SET avaliacao_id = ?, estudante_id = ?, administrador_id = ?, denuncia = ? WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, (*denuncia, id))
        self.conn.commit()

    def delete_denuncia(self, id):
        sql = 'DELETE FROM Denuncias WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()