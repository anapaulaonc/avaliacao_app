from flask import Flask, render_template, url_for, flash, redirect, request, session
from werkzeug.security import generate_password_hash
import sqlite3



from flask_login import UserMixin, LoginManager, login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField



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
    

def get_post(id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM Avaliacoes WHERE id = ?', (id,)).fetchone()
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
    try:
        cur.execute("SELECT * FROM Turmas")
        turmas = cur.fetchall()
    except Exception as e:
        print(e)
        
    conn.close()

    return render_template('main.html', turmas=turmas)

@app.route('/ver_avaliacoes', methods=['GET'])
def ver_avaliacoes(turma_id):
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
                print(estudante['senha'])
                flash('Senha incorreta!', 'danger')
        else:
            print('Email incorreto!')
            flash('Email incorreto!', 'danger')

    return render_template('login.html')



#     if form.validate_on_submit():
#         user = Estudante.query.filter_by(email=form.email.data).first()
#         if user:
#             if user.senha == form.senha.data:
#                 flash('Logado com sucesso!', 'success')
#                 return redirect(url_for('home'))
#             else:
#                 flash('Senha incorreta!', 'danger')
#         else:
#             flash('Email incorreto!', 'danger')
    
#     return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        email = request.form.get('email')
        matricula = request.form.get('matricula')
        curso = request.form.get('curso')
        senha = request.form.get('senha')
        e_administrador = request.form.get('e_administrador') in ['true', 'True', '1', 'on']

        conn = get_db_connection()

        conn.execute("INSERT INTO Estudantes (email, matricula, curso, senha, e_administrador) VALUES (?, ?, ?, ?, ?)",
                    (email, matricula, curso, senha, e_administrador))
        conn.commit()
        conn.close()

        session['matricula'] = matricula
        session['email'] = email
        session['curso'] = curso
        session['senha'] = senha
        print('AQUI A SENHA:')
        print(session['senha'])
        
        return redirect(url_for('main'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)