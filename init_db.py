import sqlite3
from models.estudante_dao import EstudanteDAO
from models.professor_dao import ProfessorDAO
from models.departamento_dao import DepartamentoDAO
from models.disciplina_dao import DisciplinaDAO
from models.turma_dao import TurmaDAO
from models.avaliacao_dao import AvaliacaoDAO
from models.denuncia_dao import DenunciaDAO

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Populando a tabela Estudantes            

estudante_dao = EstudanteDAO('database.db')

estudantes = [
    ('email1@unb.br', 'matricula1', 'curso1', 'senha1', 0),
    ('email2@unb.br', 'matricula2', 'curso2', 'senha2', 1),
    ('email3@unb.br', 'matricula3', 'curso3', 'senha3', 1),

]

for estudante in estudantes:
    estudante_dao.insert_estudante(estudante)

estudante_dao.close()

# Populando a entidade Professores
professor_dao = ProfessorDAO('database.db')

professores = [
    ('Professor 1', 1),
    ('Professor 2', 1),
    ('Professor 3', 2),
    ('Professor 4', 2),

]

for professor in professores:
    professor_dao.insert_professor(professor)

professor_dao.close()   

#Populando a tabela Departamentos
departamento_dao = DepartamentoDAO('database.db')

departamentos = [
    ('Departamento 1',),
    ('Departamento 2',),
    ('Departamento 3',),
]

for departamento in departamentos:
    departamento_dao.insert_departamento(departamento)

departamento_dao.close()

#Populando a tabela Disciplinas

disciplina_dao = DisciplinaDAO('database.db')

disciplinas = [
    ('Disciplina 1', 1),
    ('Disciplina 2', 1),
    ('Disciplina 3', 2),

]

for disciplina in disciplinas:
    disciplina_dao.insert_disciplina(disciplina)

disciplina_dao.close()

#Populando a tabela Turmas

turma_dao = TurmaDAO('database.db')

turmas = [
    (1, 1),
    (2, 2),
    (3, 3),
]
for turma in turmas:
    turma_dao.insert_turma(turma)

turma_dao.close()


#Populando a tabela Avaliacoes

avaliacao_dao = AvaliacaoDAO('database.db')

avaliacoes = [
    (1, 1, 'Avaliação 1'),
    (2, 2, 'Avaliação 2'),
    (3, 3, 'Avaliação 3'),
]

for avaliacao in avaliacoes:
    avaliacao_dao.insert_avaliacao(avaliacao)

avaliacao_dao.close()

#Populando a tabela Denuncias


denuncia_dao = DenunciaDAO('database.db')

denuncias = [
    (1, 1, 1, 'Denuncia 1'),
    (2, 2, 1, 'Denuncia 2'),
    (3, 3, 1, 'Denuncia 3'),
]


for denuncia in denuncias:
    denuncia_dao.insert_denuncia(denuncia)

denuncia_dao.close()            


# connection = sqlite3.connect('database.db')


# cur = connection.cursor()

# cur.execute("""INSERT INTO Departamentos (nome) VALUES ('MAT'), ('CIC'), ('FIS'), ('QUI') """)
# cur.execute("""INSERT INTO Professores (nome, departamento_id) VALUES ('João', 1), ('Maria', 2), ('JosE', 3), ('Ana', 4) """)
# cur.execute("""INSERT INTO Disciplinas (nome, departamento_id) VALUES ('CAL', 1), ('FTC',2), ('FIS', 3), ('QUI', 4) """)
# cur.execute("""INSERT INTO Turmas (numero, disciplina_id, professor_id) VALUES (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4) """)
# cur.execute("""INSERT INTO Estudantes (email, matricula, curso, senha, e_administrador) VALUES ('anaponc@gmail.com', '190142120', 'cic', '123', 1), ('brenno@gmail.com', '190142121', 'fis', '123', 0), ('leo@gmail.com', '190142122', 'cic', '123', 0)""")
# cur.execute("""INSERT INTO Avaliacoes (comentario, estudante_id, turma_id, avaliacao) VALUES ('Muito bom', 1, 1, '5'), ('Muito ruim', 2, 2, '1'), ('Bom', 3, 3, '4') """)

# connection.commit()
# connection.close()
        

        