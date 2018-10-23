

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'you-will-never-guess'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql+pymysql://root:jinzhen.1985@localhost/jin_obs_segy?charset=utf8"

login_manager.login_view = "login"
db = SQLAlchemy(app)