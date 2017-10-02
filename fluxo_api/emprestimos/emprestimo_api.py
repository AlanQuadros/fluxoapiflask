from flask import jsonify, Blueprint

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
