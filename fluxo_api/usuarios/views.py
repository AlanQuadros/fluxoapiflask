from operator import and_

from flask import jsonify, Blueprint

from fluxo_api.usuarios.models import User

users = Blueprint('usuarios', __name__)

@users.route('/')
@users.route('/home')
def home():
    return "API Fluxo AGES em Python usando Flask."

@users.route('/usuarios')
@users.route('/usuarios/')
def mostrar_todos_usuarios():
    users = User.query.order_by(User.id_usuario.asc()).all()

    output = []

    for user in users:
        user_data = {}
        user_data['id_usuario'] = user.id_usuario
        user_data['usuario'] = user.usuario
        user_data['perfil_acesso'] = user.perfil_acesso
        user_data['status_usuario'] = user.status_usuario
        user_data['id_tipo_usuario'] = user.id_tipo_usuario
        user_data['matricula'] = user.matricula
        user_data['nome'] = user.nome
        user_data['email'] = user.email
        user_data['usuario_gitlab'] = user.usuario_gitlab
        user_data['data_inclusao'] = user.data_inclusao
        output.append(user_data)

    return jsonify({'Usuarios': output})

@users.route('/usuarios/id/<id>', methods=['GET'])
def buscar_usuario_id(id):
    usuario = User.query.filter_by(id_usuario=id).first()

    if not usuario:
        return jsonify({"message": "Usuario nao encontrado!"})

    user_data = {}
    user_data['id_usuario'] = usuario.id_usuario
    user_data['usuario'] = usuario.usuario
    user_data['perfil_acesso'] = usuario.perfil_acesso
    user_data['status_usuario'] = usuario.status_usuario
    user_data['id_tipo_usuario'] = usuario.id_tipo_usuario
    user_data['matricula'] = usuario.matricula
    user_data['nome'] = usuario.nome
    user_data['email'] = usuario.email
    user_data['usuario_gitlab'] = usuario.usuario_gitlab
    user_data['data_inclusao'] = usuario.data_inclusao

    return jsonify({"Usuarios": user_data})

@users.route('/usuarios/matricula/<mat>', methods=['GET'])
def buscar_usuario_matricula(mat):
    usuario = User.query.filter_by(matricula=mat).first()

    if not usuario:
        return jsonify({"message": "Usuario nao encontrado!"})

    user_data = {}
    user_data['id_usuario'] = usuario.id_usuario
    user_data['usuario'] = usuario.usuario
    user_data['perfil_acesso'] = usuario.perfil_acesso
    user_data['status_usuario'] = usuario.status_usuario
    user_data['id_tipo_usuario'] = usuario.id_tipo_usuario
    user_data['matricula'] = usuario.matricula
    user_data['nome'] = usuario.nome
    user_data['email'] = usuario.email
    user_data['usuario_gitlab'] = usuario.usuario_gitlab
    user_data['data_inclusao'] = usuario.data_inclusao

    return jsonify({"Usuarios": user_data})


# Alunos
@users.route('/alunos')
@users.route('/alunos/')
def mostrar_todos_alunos():
    alunos = (User.query
              .filter_by(id_tipo_usuario=2)
              .order_by(User.id_usuario.asc())
              .all())

    output = []

    for user in alunos:
        user_data = {}
        user_data['id_usuario'] = user.id_usuario
        user_data['usuario'] = user.usuario
        user_data['status_usuario'] = user.status_usuario
        user_data['id_tipo_usuario'] = user.id_tipo_usuario
        user_data['matricula'] = user.matricula
        user_data['nome'] = user.nome
        user_data['email'] = user.email
        output.append(user_data)

    return jsonify({'Alunos': output})

@users.route('/alunos/id/<id>', methods=['GET'])
def buscar_aluno_id(id):
    aluno = (User.query
             .filter(and_(User.id_usuario==id, User.id_tipo_usuario==2))
             .first())

    if not aluno:
        return jsonify({"message": "Aluno nao encontrado!"})

    user_data = {}
    user_data['id_usuario'] = aluno.id_usuario
    user_data['usuario'] = aluno.usuario
    user_data['status_usuario'] = aluno.status_usuario
    user_data['id_tipo_usuario'] = aluno.id_tipo_usuario
    user_data['matricula'] = aluno.matricula
    user_data['nome'] = aluno.nome
    user_data['email'] = aluno.email

    return jsonify({"Alunos": user_data})

@users.route('/alunos/matricula/<mat>', methods=['GET'])
def buscar_aluno_matricula(mat):
    aluno = (User.query
             .filter(and_(User.matricula == mat, User.id_tipo_usuario == 2))
             .first())

    if not aluno:
        return jsonify({"message": "Usuario nao encontrado!"})

    user_data = {}
    user_data['id_usuario'] = aluno.id_usuario
    user_data['usuario'] = aluno.usuario
    user_data['status_usuario'] = aluno.status_usuario
    user_data['id_tipo_usuario'] = aluno.id_tipo_usuario
    user_data['matricula'] = aluno.matricula
    user_data['nome'] = aluno.nome
    user_data['email'] = aluno.email

    return jsonify({"Alunos": user_data})