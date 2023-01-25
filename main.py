# ORM (Object Relational Mapping - обьектно реляционное отображение) - технология которая связывает БД с концепциями обьектно ориентированых языков программирования. ORM-прослойка между БД и кодом который пишет программист, которая похволяет создавать в программе обьекты обновлять, удалять получать их.


#python ORM:
    # peewee
    # sqlalchemy
    # DjangoORM

# Класс - Таблица в БД
# Атрибут класса - поле в БД 
# Обьект класса - строка в таблице 

# pip install peewee 

from views import *
from settings import db


# print('=====================================')
# print('=====================================')
# get_products()
# detail_category(1)


db.connect()


get_products()


db.close()
