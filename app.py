from flask import Flask, render_template, url_for, flash, redirect, request, session
from werkzeug.security import generate_password_hash
import sqlite3



app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_student(student_id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM Estudantes WHERE id = ?',
                        (student_id,)).fetchone()
    conn.close()
    return student

def get_professor(professor_id):
    conn = get_db_connection()
    professor = conn.execute('SELECT * FROM Professores WHERE id = ?',
                        (professor_id,)).fetchone()
    conn.close()
    return professor

def get_disciplina(disciplina_id):
    conn = get_db_connection()
    disciplina = conn.execute('SELECT * FROM Disciplinas WHERE id = ?',
                        (disciplina_id,)).fetchone()
    conn.close()
    return disciplina

def get_turma(turma_id):
    conn = get_db_connection()
    turma = conn.execute('SELECT * FROM Turmas WHERE id = ?', 
                        (turma_id,)).fetchone()
    conn.close()
    return turma
    

def get_avaliacao(avaliacao_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM Avaliacoes WHERE id = ?', (avaliacao_id,)).fetchone()
    conn.close()
    return post




# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     senha = PasswordField('Senha', validators=[DataRequired()])
#     submit = SubmitField('Logar')

# class RegisterForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     matricula = StringField('Matricula', validators=[DataRequired()])
#     curso = StringField('Curso', validators=[DataRequired()])
#     senha = PasswordField('Senha', validators=[DataRequired()])
#     submit = SubmitField('Registrar')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    conn = get_db_connection()
    cur = conn.cursor()

    #ter todos os professores
    cur.execute("SELECT * FROM Avaliacoes")
    avaliacoes = cur.fetchall()
    cur.execute("SELECT * FROM Professores")
    professores = cur.fetchall()
    cur.execute("SELECT * FROM Turmas")
    turmas = cur.fetchall()
    cur.execute("SELECT * FROM Estudantes")
    estudantes = cur.fetchall()
    # Executa a consulta usando JOIN entre as tabelas Avaliacoes, Estudantes, Disciplinas e Turmas
    cur.execute('SELECT Avaliacoes.avaliacao, Estudantes.email, Disciplinas.nome, Turmas.id FROM Avaliacoes JOIN Estudantes ON Avaliacoes.estudante_id = Estudantes.id JOIN Turmas ON Avaliacoes.turma_id = Turmas.id JOIN Disciplinas ON Turmas.disciplina_id = Disciplinas.id')

    # Recupera os resultados da consulta
    results = cur.fetchall()



        
    conn.close()

    return render_template('main.html', avaliacoes=avaliacoes, professores=professores, turmas=turmas, estudantes=estudantes, results=results)


@app.route('/avaliar/<turma_id>', methods=['GET', 'POST'])
def avaliar(turma_id):
    conn = get_db_connection()
    cur = conn.cursor()

    #ter todas as avaliacoes do professor
    cur.execute("SELECT * FROM Avaliacoes WHERE turma_id = ?", (turma_id,))

    avaliacoes = cur.fetchall()
    conn.close()

    return render_template('avaliacao.html', avaliacoes=avaliacoes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        

        conn = get_db_connection()
        estudante = conn.execute('SELECT * FROM Estudantes WHERE email = ?',
                        (email,)).fetchone()
        print(estudante)
        conn.close()

        if estudante:
            if estudante['senha'] == senha:
                session['matricula'] = estudante['matricula']
    
                return redirect(url_for('main'))
            else:
  
                flash('Senha incorreta!', 'danger')
        else:
            print('Email incorreto!')
            flash('Email incorreto!', 'danger')

    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        email = request.form.get('email')
        matricula = request.form.get('matricula')
        curso = request.form.get('curso')
        senha = request.form.get('senha')

        conn = get_db_connection()

        conn.execute("INSERT INTO Estudantes (email, matricula, curso, senha, e_administrador) VALUES (?, ?, ?, ?, ?)",
                    (email, matricula, curso, senha))
        conn.commit()
        conn.close()

        session['matricula'] = matricula
        session['email'] = email
        session['curso'] = curso
        session['senha'] = senha
    
        
        return redirect(url_for('main'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)