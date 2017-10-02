from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from fluxo_api.usuarios.views import users
from fluxo_api.equipamentos.views import equipamentos
from fluxo_api.emprestimos.emprestimo_api import emprestimos

app.register_blueprint(users)
app.register_blueprint(equipamentos)
app.register_blueprint(emprestimos)

# db.create_all()