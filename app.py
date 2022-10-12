from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from model.BaseModel import BaseModel

from classes.EngineConnect import EngineConnect

app = Flask(__name__)
app.config.from_object('config.common')

db = SQLAlchemy(app)
Model = db.Model
migrate = Migrate(app, db)

engine = EngineConnect()

if __name__ == '__main__':
    app.run()

