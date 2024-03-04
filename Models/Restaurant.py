from mongoengine import Document, StringField, ReferenceField, ListField

class Restaurant(Document):
    name = StringField(required=True, unique=True)
    address = StringField(required=True)
    dishes=ListField(ReferenceField('Dish'))
