import os
SECRET_KEY='alura' #para utilizar session, secret key é obrigatório, para criptografar dados e não guardar informações confidenciais no navegador

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector', #mesmo se mudarmos a ORM, é só trocar aqui
        usuario = 'root',
        senha = 'wqd2tyy87',
        servidor = 'localhost',
        database = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'