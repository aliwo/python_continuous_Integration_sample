from tortoise import Model, fields

from database.base import Base


class Memo(Base, Model):

    title = fields.CharField(max_length=40, null=False)
    body = fields.TextField(null=False)

    class Meta:
        table = "memos"
