from flask import jsonify, Blueprint

from fluxo_api.equipamentos.models import Equipamento

equipamentos = Blueprint('equipamentos', __name__)

@equipamentos.route('/equipamentos')
@equipamentos.route('/equipamentos/')
def mostrar_todos():
    equipamentos = Equipamento.query.order_by(Equipamento.id_equipamento.asc()).all()

    output = []

    for equip in equipamentos:
        equip_data = {}
        equip_data['id_equipamento'] = equip.id_equipamento
        equip_data['nome'] = equip.nome
        equip_data['numero'] = equip.numero
        equip_data['codigo'] = equip.codigo
        equip_data['descricao'] = equip.descricao
        equip_data['data_movimentacao'] = equip.data_movimentacao
        equip_data['id_tipo_equipamento'] = equip.id_tipo_equipamento
        equip_data['status'] = equip.status
        output.append(equip_data)

    return jsonify({'Equipamentos': output})

@equipamentos.route('/equipamentos/id/<id>', methods=['GET'])
def buscar_equipamento_id(id):
    equipamento = Equipamento.query.filter_by(id_equipamento=id).first()

    if not equipamento:
        return jsonify({'message' : 'Equipamento nao encontrado!'})

    equip_data = {}
    equip_data['id_equipamento'] = equipamento.id_equipamento
    equip_data['nome'] = equipamento.nome
    equip_data['numero'] = equipamento.numero
    equip_data['codigo'] = equipamento.codigo
    equip_data['descricao'] = equipamento.descricao
    equip_data['data_movimentacao'] = equipamento.data_movimentacao
    equip_data['id_tipo_equipamento'] = equipamento.id_tipo_equipamento
    equip_data['status'] = equipamento.status

    return jsonify({'Equipamentos': equip_data})

@equipamentos.route('/equipamentos/numero/<numero>', methods=['GET'])
def buscar_equipamento_numero(numero):
    equipamento = Equipamento.query.filter_by(numero=numero).first()

    if not equipamento:
        return jsonify({'message' : 'Equipamento nao encontrado!'})

    equip_data = {}
    equip_data['id_equipamento'] = equipamento.id_equipamento
    equip_data['nome'] = equipamento.nome
    equip_data['numero'] = equipamento.numero
    equip_data['codigo'] = equipamento.codigo
    equip_data['descricao'] = equipamento.descricao
    equip_data['data_movimentacao'] = equipamento.data_movimentacao
    equip_data['id_tipo_equipamento'] = equipamento.id_tipo_equipamento
    equip_data['status'] = equipamento.status

    return jsonify({'Equipamentos': equip_data})