from datetime import datetime

from flask import jsonify, Blueprint, request

from fluxo_api import db
from fluxo_api.emprestimos.emprestimo import Emprestimo

emprestimos = Blueprint('emprestimos', __name__)

@emprestimos.route('/emprestimos')
@emprestimos.route('/emprestimos/')
def mostrar_todos():
    emps = Emprestimo.query.order_by(Emprestimo.id_equip_aluno.asc()).all()

    output = []

    for emp in emps:
        data = {}
        data['id_equip_aluno'] = emp.id_equip_aluno
        data['id_equipamento'] = emp.id_equipamento
        data['id_usuario'] = emp.id_usuario
        data['observacao'] = emp.observacao
        data['data_retirada'] = emp.data_retirada
        data['data_entrega'] = emp.data_entrega
        output.append(data)

    return jsonify({'Emprestimos': output})

@emprestimos.route('/emprestimos', methods=['POST'])
def criar_emprestimo():
    data = request.get_json()

    equip_em_uso = (Emprestimo.query
                    .filter(Emprestimo.data_entrega == None, Emprestimo.id_equipamento == data['id_equipamento']).
                    count())

    if equip_em_uso:
        return jsonify({"erro":"Equipamento em uso!"})

    novo_emprestimo = Emprestimo(data['id_equipamento'], data['id_usuario'], datetime.utcnow())

    db.session.add(novo_emprestimo)
    db.session.commit()

    return jsonify({'messagem': 'Emprestimo cadastrado com sucesso!'})