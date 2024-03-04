from mongoengine import Document, ReferenceField, StringField, ListField

class Order(Document):
    user = ReferenceField("User", required=True)
    restaurant = ReferenceField("Restaurant", required=True)
    dishes = ListField(ReferenceField("Dish"), required=True)
    total_price = StringField()
