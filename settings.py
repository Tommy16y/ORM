import peewee

db = peewee.PostgresqlDatabase (
    'orm_py25',
    user='postgres',
    password = '123',
    host= 'localhost',
    port = 5432

)