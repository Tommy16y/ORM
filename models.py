import peewee
from datetime import datetime
from settings import db



class Category(peewee.Model):
    id = peewee.PrimaryKeyField()
    name= peewee.CharField(max_length=100, unique=True)
    created_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'category'

class Product(peewee.Model):
    name = peewee.CharField(max_length=100)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=10)
    amount = peewee.IntegerField(null=False)
    category = peewee.ForeignKeyField(Category, related_name='products', to_field='id', on_delete='cascade')

    class Meta:
        database = db
        db_table = 'product'