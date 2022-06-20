from flask_restful import Resource, reqparse
from noteModel import NoteModel

_note_create = reqparse.RequestParser()
default_help =  'This field cannot be empty'
_note_create.add_argument('title', type=str, required=True, help=default_help)
_note_create.add_argument('content', type=str, required=True, help=default_help)

class NoteGet(Resource):
    def get(self):
        all_notes = NoteModel.find_all()
        parse_notes = [note.json() for note in all_notes]
        return {"notes": parse_notes}, 200

class NoteResource(Resource):
    def post(self):
        data = _note_create.parse_args()
        if NoteModel.find_by_title(data["title"]):
            return {"message": "A note with this title already exists"}, 400
        print(data)
        note = NoteModel(**data)
        note.save_to_db()
        return {"message": "Note created successfully"}, 201

class DeleteNote(Resource):
    def delete(self, _id):
        note = NoteModel.find_by_id(_id)
        if note:
            note.delete_from_db()
            return {"message": "Note deleted successfully"}, 200
        return {"message": "Note not found"}, 404

