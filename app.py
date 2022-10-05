from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from classes.EngineConnect import EngineConnect

app = Flask(__name__)
app.config.from_object('config.common')

db = SQLAlchemy(app)
Model = db.Model
migrate = Migrate(app, db)

engine = EngineConnect()

if __name__ == '__main__':
    # app.run()
    #
    # result = engine.engine.engine.execute("""
    #     SELECT * FROM "doctors"
    # """)
    #
    #
    # columns_name = result.keys()
    # data_in_db = result.fetchall()[::-1]
    #
    # for column in columns_name:
    #     print(column, end="|\t")
    #
    # print('\n--------------------------------------')
    #
    # for data in data_in_db:
    #     for item in data:
    #         print(item, end="|\t")
    #     print('\n')
