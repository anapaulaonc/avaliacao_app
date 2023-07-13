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
           
def populate_db():
    # Cria os objetos DAO
    estudante_dao = EstudanteDAO('database.db')
    professor_dao = ProfessorDAO('database.db')
    disciplina_dao = DisciplinaDAO('database.db')
    turma_dao = TurmaDAO('database.db')
    departamento_dao = DepartamentoDAO('database.db')
    avaliacao_dao = AvaliacaoDAO('database.db')
    denuncia_dao = DenunciaDAO('database.db')

    # Insere dados na tabela Departamentos
    departamento_dao.insert_departamento(("Departamento de Matemática",))
    departamento_dao.insert_departamento(("Departamento de Física",))
    departamento_dao.insert_departamento(("Departamento de Química",))

    # Insere dados na tabela Professores
    professor_dao.insert_professor(("Professor Matemática", 1))
    professor_dao.insert_professor(("Professor Física", 2))
    professor_dao.insert_professor(("Professor Química", 3))

    # Insere dados na tabela Disciplinas
    disciplina_dao.insert_disciplina(("Matemática Básica", 1))
    disciplina_dao.insert_disciplina(("Física Básica", 2))
    disciplina_dao.insert_disciplina(("Química Básica", 3))

    # Insere dados na tabela Turmas
    turma_dao.insert_turma((1, 1))
    turma_dao.insert_turma((2, 2))
    turma_dao.insert_turma((3, 3))

    # Insere dados na tabela Estudantes
    estudante_dao.insert_estudante(("estudante1@unb.br", "123456", "Matemática", "senha", 0))
    estudante_dao.insert_estudante(("estudante2@unb.br", "234567", "Física", "senha", 0))
    estudante_dao.insert_estudante(("estudante3@unb.br", "345678", "Química", "senha", 0))
    estudante_dao.insert_estudante(("admin@unb.br", "admin", "Administração", "senha", 1))

    # Insere dados na tabela Avaliações
    avaliacao_dao.insert_avaliacao((1, 1, "Ótima aula!"))
    avaliacao_dao.insert_avaliacao((2, 2, "Bom conteúdo, mas difícil."))
    avaliacao_dao.insert_avaliacao((3, 3, "Precisa melhorar a didática."))

    # Insere dados na tabela Denuncias
    denuncia_dao.insert_denuncia((1, 1, 4, "Comentário ofensivo."))
    denuncia_dao.insert_denuncia((2, 2, 4, "Spam nos comentários."))
    denuncia_dao.insert_denuncia((3, 3, 4, "Conteúdo inapropriado."))