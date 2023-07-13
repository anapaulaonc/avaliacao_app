import sqlite3
from sqlite3 import Error 

class DepartamentoDAO:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.execute('PRAGMA foreign_keys = 1')

    def insert_departamento(self, departamento):
        sql = ''' INSERT INTO Departamentos(nome)
                  VALUES(?) '''
        cur = self.conn.cursor()
        cur.execute(sql, departamento)
        self.conn.commit()
        return cur.lastrowid

    def update_departamento(self, nome, id):
        sql = ''' UPDATE Departamentos SET nome = ? WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, (nome, id))
        self.conn.commit()

    def delete_departamento(self, id):
        sql = 'DELETE FROM Departamentos WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
