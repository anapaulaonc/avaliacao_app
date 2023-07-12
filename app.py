from flask import Flask, render_template, url_for, flash, redirect
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import UserMixin



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)


#model
engine = create_engine('sqlite:///database.db')
Base = declarative_base()

class Estudantes(Base):
    _tablename_ = 'Estudantes'

    email = Column(String, primary_key=True)
    matricula = Column(String)
    curso = Column(String)
    senha = Column(String)
    e_administrador = Column(Boolean)

Base.metadata.create_all(bind=engine)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Logar')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    matricula = StringField('Matricula', validators=[DataRequired()])
    curso = StringField('Curso', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Registrar')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Estudante.query.filter_by(email=form.email.data).first()
        if user:
            if user.senha == form.senha.data:
                flash('Logado com sucesso!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Senha incorreta!', 'danger')
        else:
            flash('Email incorreto!', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Estudante(email=form.email.data, matricula=form.matricula.data, curso=form.curso.data, senha=form.senha.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)