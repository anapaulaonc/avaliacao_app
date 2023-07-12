from sqlalchemy import create_engine, text 

engine = create_engine('sqlite:///database.db', echo=True)

with engine.connect() as connection:
   
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS Estudantes (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            matricula TEXT NOT NULL,
            curso TEXT NOT NULL,
            senha TEXT NOT NULL,
            e_administrador BOOLEAN NOT NULL DEFAULT 0
        )
    """))
    connection.execute(text("""

        CREATE TABLE IF NOT EXISTS Professores (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            departamento_id INTEGER,
            FOREIGN KEY (departamento_id) REFERENCES Departamentos (id)
        )
    """))
    connection.execute(text("""

        CREATE TABLE IF NOT EXISTS Disciplinas (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            departamento_id INTEGER,
            FOREIGN KEY (departamento_id) REFERENCES Departamentos (id)
        )
    """))
    connection.execute(text("""

        CREATE TABLE IF NOT EXISTS Turmas (
            id INTEGER PRIMARY KEY,
            disciplina_id INTEGER,
            professor_id INTEGER,
            FOREIGN KEY (disciplina_id) REFERENCES Disciplinas (id),
            FOREIGN KEY (professor_id) REFERENCES Professores (id)
        )
    """))
    
    connection.execute(text("""

        CREATE TABLE IF NOT EXISTS Departamentos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """))
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS Avaliacoes (
            id INTEGER PRIMARY KEY,
            estudante_id INTEGER,
            turma_id INTEGER,
            avaliacao TEXT NOT NULL,
            FOREIGN KEY (estudante_id) REFERENCES Estudantes (id),
            FOREIGN KEY (turma_id) REFERENCES Turmas (id)
        )
    """))

    connection.execute(text("""

        CREATE TABLE IF NOT EXISTS Denuncias (
            id INTEGER PRIMARY KEY,
            avaliacao_id INTEGER,
            estudante_id INTEGER,
            administrador_id INTEGER,
            denuncia TEXT NOT NULL,
            FOREIGN KEY (avaliacao_id) REFERENCES Avaliacoes (id),
            FOREIGN KEY (estudante_id) REFERENCES Estudantes (id),
            FOREIGN KEY (administrador_id) REFERENCES Estudantes (id)
        )
    """))

        