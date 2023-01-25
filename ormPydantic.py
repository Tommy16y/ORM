import pydantic
import peewee
from playhouse.db_url import connect
from typing import List
 
db = peewee.PostgresqlDatabase (
    'orm_py25',
    user='postgres',
    password = '123',
    host= 'localhost',
    port = 5432

)
 
 
class BaseModel(peewee.Model):
    class Meta:
        database = db
 
 
class User(BaseModel):
    id = peewee.AutoField()
    name = peewee.CharField(max_length=255)
 
 
class Post(BaseModel):
    id = peewee.AutoField()
    title = peewee.CharField(max_length=255)
    content = peewee.TextField()
    author = peewee.ForeignKeyField(User, backref="posts")
 
 
class Tag(BaseModel):
    id = peewee.AutoField()
    name = peewee.CharField(max_length=255)
    posts = peewee.ManyToManyField(Post, backref="tags")
 
 
class UserModel(pydantic.BaseModel):
    class Config:
        orm_mode = True
        
        id: int
        name: pydantic.constr(max_length=255)
 
 
class PostModel(pydantic.BaseModel):
    class Config:
        orm_mode = True
 
        id: int
        title: pydantic.constr(max_length=255)
        content: str
        author: UserModel
    class Config:
        orm_mode = True
 
        id: int
        name: pydantic.constr(max_length=255)
 
 
 
 
class TagModel(pydantic.BaseModel):
    class Config:
        orm_mode = True
 
        id: int
        name: pydantic.constr(max_length=255)
 
 
if __name__ == "__main__":
    # Setup the schema
    PostTag = Post.tags.get_through_model() # join table
    db.create_tables([User, Post, Tag, PostTag])
    
    with db.atomic(): # Wrap operations in a transaction
    # Create user
        user = User(name="João Victor")
        user.save()
    
    # Create a post associated with the user
    post = Post(title="First blog",
    content="Hello world",
    author=user)
    post.save()
    
    # Create tags associated with the user
    tag = Tag(name="test")
    tag.save()
    
    tag2 = Tag(name="hello-world")
    tag2.save()
    
    post.tags.add([tag, tag2])
    
    # Load all posts with users and tags loaded via eager-loading
    posts = Post.select()\
    .join(User)\
    .switch(Post)\
    .join(PostTag)\
    .join(Tag)\
    .paginate(10, 1)
 
    for post in posts:
        print(PostModel.from_orm(post))
        tags = [TagModel.from_orm(tag) for tag in post.tags]
        print("Tags: " + ", ".join([tag.name for tag in tags]))