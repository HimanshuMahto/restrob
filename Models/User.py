from mongoengine import Document, StringField, ReferenceField, ListField

class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    phone_number = StringField(required=True, unique=True)
    address = StringField()
    orders = ListField(ReferenceField('Order'))