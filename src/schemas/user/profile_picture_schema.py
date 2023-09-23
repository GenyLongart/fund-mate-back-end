from marshmallow import Schema, fields, validates_schema
from ..master_schema import MasterSchema

class ProfilePictureSchema(Schema):
    profilePictureFile = fields.Field(metadata={'type': 'string', 'format': 'byte'}, required=True)

    @validates_schema
    def masterSchemaInvoke(self, in_data, **kwargs):
        masterSchema = MasterSchema()
        return masterSchema.validate_uploaded_file(in_data, "profilePictureFile", ["image/png", "image/jpeg"])