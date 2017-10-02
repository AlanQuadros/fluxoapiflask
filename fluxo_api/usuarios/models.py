from fluxo_api import db

class User(db.Model):
    __tablename__ = 'tb_usuario'
    id_usuario = db.Column('id_usuario', db.Integer, primary_key=True)
    usuario = db.Column(db.String(45))
    senha = db.Column(db.String(45))
    perfil_acesso = db.Column(db.String(20))
    status_usuario = db.Column(db.String(20))
    id_tipo_usuario = db.Column(db.Integer)
    matricula = db.Column(db.String)
    nome = db.Column(db.String(60))
    email = db.Column(db.String)
    usuario_gitlab = db.Column(db.String(45))
    data_inclusao = db.Column(db.DateTime)

    def __init__(self, usuario, senha, perfil_acesso, status_usuario, id_tipo_usuario,
                 matricula, nome, email, usuario_gitlab, data_inclusao):
        self.usuario = usuario
        self.senha = senha
        self.perfil_acesso = perfil_acesso
        self.status_usuario = status_usuario
        self.id_tipo_usuario = id_tipo_usuario
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.usuario_gitlab = usuario_gitlab
        self.data_inclusao = data_inclusao

    def __repr__(self):
        return '<Usuario %d>' % self.id_usuario