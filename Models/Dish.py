from mongoengine import Document, StringField, ReferenceField, ListField

class Dish(Document):
    name = StringField(required=True)
    description = StringField()
    price = StringField(reqquired=True)
    category = StringField(choices=["veg", "non-veg"], required=True)
