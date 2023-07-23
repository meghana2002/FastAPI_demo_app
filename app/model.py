from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(default=None)
    title: str = Field(default = None)
    content : str = Field(default = None)
    class Config:
        schema_extra = {
            "post_demo":{
                "title": "Some title about animals",
                "content":"Some content about animals"
            }
        }

class UserSchema(BaseModel):
    #id : int = Field(default=None)
    fullname: str = Field(default=None)
    email : EmailStr = Field(default = None)
    password: str = Field(default = None)
    class Config:
        schema_extra = {
            "user-demo" : {
                "name": "Bek",
                "email": "bek12345@brace.com",
                "password": "123"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default = None)
    password: str = Field(default = None)
    class Config:
        schema_extra = {
            "user-demo" : {
                "email": "bek12345@brace.com",
                "password": "123"
            }
        }