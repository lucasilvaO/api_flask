from api import ma
from marshmallow import Schema, fields

class DescriptionSchema(Schema):
    region = fields.Str(required=True)
    faction = fields.Str(required=True)
    important_battle = fields.Str(required=True)

class LoreSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'name', 'race', 'description')
        
    _id = fields.Str()
    name = fields.Str(required=True)
    race = fields.Str(required=True)
    description = fields.Nested(DescriptionSchema, required=True)
