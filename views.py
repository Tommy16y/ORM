import peewee
from datetime import datetime
from models import Category,Product

def post_category(category_name):
    try:
        category = Category(name=category_name)
        category.save()
        print('SAVED@!')
    except peewee.IntegrityError:
        print('ТАКАЯ КАТЕГОРИЯ УЖЕ ЕСТЬ!')

def get_categories():
    categories = Category.select()
    for category in categories:
        print(f'|--{category.id}--{category.name}--{category.created_at}--|')
        

def delete_category(category_id):
    try:
        category = Category.get(id=category_id)
        category.delete_instance()
        print('DELETEED!!!!')
    except peewee.DoesNotExist:
        print('Категория не найдена!!!')

def update_category(category_id,new_name):
    try:
        category = Category.get(id=category_id)
        category.name = new_name
        category.save
        print('updated!')
    except peewee.DoesNotExist:
        print('Категория не найдена!!')

def detail_category(id_category):
    try:
        category = Category.get(id=id_category)
        print(category.id, end=' ')
        print(category.name, end=' ')
        print(category.created_at,end=' ')
        for i in category.products:
            print(f'|{i.name}--{i.price}--{i.amount}|')
    except peewee.DoesNotExist:
        print('нет такой категории')

    
    

def post_product(product_name,product_price,product_amount,product_category):
    product = Product(name=product_name,price=product_price,amount=product_amount,category=product_category)
    product.save()
    print('ВСЕ ОК ')

def delete_products(product_name):
    try:
        product = Product.get(name=product_name)
        product.delete_instance()
        print('DELETED!!')
    except peewee.DoesNotExist:
        print('Категория не найдена!!')

def update_product(product_name,new_price):
    try:
        product = Product.get(name=product_name)
        product.name = new_price
        print('updated!!')
    except peewee.DoesNotExist:
        print('Категория не найдена!!')
def get_product_by_name(name):
    products = Product.select().where(Product.name==name)
    for i in products:
        print(i.name, i.price)
    
def get_products():
    products=Product.select()
    for product in products:
        print(f'|--{product.name}--{product.price}--{product.amount}--{product.category}--|')
