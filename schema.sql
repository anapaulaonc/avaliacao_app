CREATE TABLE Estudantes (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    matricula TEXT NOT NULL,
    curso TEXT NOT NULL,
    senha TEXT NOT NULL,
    e_administrador BOOLEAN NOT NULL DEFAULT 0
);

CREATE TABLE Professores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    departamento_id INTEGER,
    CONSTRAINT fk_departamento_id
    FOREIGN KEY (departamento_id) REFERENCES Departamentos (id)
);

CREATE TABLE Disciplinas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    departamento_id INTEGER,
    CONSTRAINT fk_departamento_id
    FOREIGN KEY (departamento_id) REFERENCES Departamentos (id)
);

CREATE TABLE Turmas (
    id INTEGER PRIMARY KEY,
    disciplina_id INTEGER,
    professor_id INTEGER,
    CONSTRAINT fk_disciplina_id
    FOREIGN KEY (disciplina_id) REFERENCES Disciplinas (id)
    CONSTRAINT fk_professor_id
    FOREIGN KEY (professor_id) REFERENCES Professores (id)
);

CREATE TABLE Departamentos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE Avaliacoes (
    id INTEGER PRIMARY KEY,
    estudante_id INTEGER,
    turma_id INTEGER,
    avaliacao TEXT NOT NULL,
    FOREIGN KEY (estudante_id) REFERENCES Estudantes (id),
    FOREIGN KEY (turma_id) REFERENCES Turmas (id)
);

CREATE TABLE Denuncias (
    id INTEGER PRIMARY KEY,
    avaliacao_id INTEGER,
    estudante_id INTEGER,
    administrador_id INTEGER,
    denuncia TEXT NOT NULL,
    CONSTRAINT fk_avaliacao_id
    FOREIGN KEY (avaliacao_id) REFERENCES Avaliacoes (id),
    CONSTRAINT fk_estudante_id
    FOREIGN KEY (estudante_id) REFERENCES Estudantes (id),
    CONSTRAINT fk_administrador_id
    FOREIGN KEY (administrador_id) REFERENCES Estudantes (id)
);