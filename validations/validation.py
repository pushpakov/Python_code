from marshmallow import Schema, fields, post_load
from models.model import Person

# Marshmallow schema
class PersonSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    followers = fields.List(fields.Raw())

    @post_load
    def make_person(self, data, **kwargs):
        return Person(**data)

