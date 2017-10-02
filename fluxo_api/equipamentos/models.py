from fluxo_api import db

class Equipamento(db.Model):
    __tablename__ = 'tb_equipamento'

    id_equipamento = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    codigo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255))
    data_movimentacao = db.Column(db.Date, nullable=False)
    id_tipo_equipamento = db.Column(db.Integer, db.ForeignKey('tb_tipo_equipamento.id_tipo_equipamento'))
    status = db.Column(db.String(15))

    def __init__(self, nome, numero, codigo, descricao, data_movimentacao, id_tipo_equipamento, status):
        self.nome = nome
        self.numero = numero
        self.codigo = codigo
        self.descricao = descricao
        self.data_movimentacao = data_movimentacao
        self.id_tipo_equipamento = id_tipo_equipamento
        self.status = status

    def __repr__(self):
        return "<Equipamento(%s,%s,%s,%s,%s,%s,%s,%s)>" % (self.id_equipamento,
                                                           self.nome,
                                                           self.numero,
                                                           self.codigo,
                                                           self.descricao,
                                                           self.data_movimentacao,
                                                           self.id_tipo_equipamento,
                                                           self.status)
