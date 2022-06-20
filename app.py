from flask import Flask
from flask_restful import Api
from db import db
from flask_cors import CORS

from noteResource import NoteResource, NoteGet, DeleteNote

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
CORS(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(NoteResource, "/notes")
api.add_resource(NoteGet, "/notes/all_notes")
api.add_resource(DeleteNote, "/notes/delete/<int:_id>")

if __name__ == '__main__':
    app.run(debug=True, port=5000)