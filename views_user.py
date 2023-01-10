from jogoteca import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima') #pega o argumento query do endereço do navegador por exemplo ?proxima=novo
    if not proxima:
        return redirect(url_for('index'))
    else:
        form = FormularioUsuario()
        return render_template('login.html', proxima=proxima, form=form) #novo variavel proxima em laranja atribuida a varivel proxima da função

@app.route('/autenticar', methods=['POST']) #mudar para post para tirar do get para não aparecer informações do usuario na barra de endereços
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha: #request form é a info dada pelo usuario
        session['usuario_logado'] = usuario.nickname  # uma sessão começada com o nick do usuário
        flash(usuario.nickname + ' logado com sucesso!')  # mensagem através da função flash, precisa alterar o arquivo html para funcionar
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))