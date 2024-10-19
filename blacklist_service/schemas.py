from marshmallow import Schema, fields


class BlacklistSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    app_uuid = fields.UUID(required=True)
    blocked_reason = fields.Str(
        required=False, validate=lambda x: len(x) <= 255)
    created_at = fields.DateTime(dump_only=True)
