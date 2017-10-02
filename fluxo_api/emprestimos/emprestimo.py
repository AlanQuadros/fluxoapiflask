from fluxo_api import db

class Emprestimo(db.Model):
    __tablename__ = 'tb_equipamento_aluno'

    id_equip_aluno = db.Column(db.Integer, primary_key=True)
    id_equipamento = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    observacao = db.Column(db.String(255))
    data_retirada = db.Column(db.DateTime)
    data_entrega = db.Column(db.DateTime)

    def __init__(self, id_equipamento, id_usuario, data_retirada):
        self.id_equipamento = id_equipamento
        self.id_usuario = id_usuario
        self.data_retirada = data_retirada

    def __repr__(self):
        return "<Emprestimo(%s,%s,%s,%s,%s,%s)>" % (self.id_equip_aluno,
                                                    self.id_equipamento,
                                                    self.id_usuario,
                                                    self.observacao,
                                                    self.data_retirada,
                                                    self.data_entrega)
