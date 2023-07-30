import uvicorn
from fastapi import FastAPI, Body, Depends
from fastapi import Request, HTTPException, Header
from sqlalchemy import Column, BIGINT, String
from db_setup import *
from app.model import PostSchema
from app.model import UserSchema
from app.model import UserLoginSchema
from app.auth.jwt_bearer import jwtBearer
from app.auth.jwt_handler import signJWT, decodeJWT
from fastapi import Depends, Header

app = FastAPI()


# Create a base class for declarative class definitions
Base = declarative_base()

# Define the table class
class PostDetails(Base):
    __tablename__ = "post_details"
    id = Column(BIGINT, primary_key=True)
    title = Column(String)
    text = Column(String)

class UserDetails(Base):
    __tablename__ = "user_details"
    name = Column(String)
    email = Column(String, primary_key=True, nullable=False)
    password = Column(String)


# Create the table
Base.metadata.create_all(engine)

# Optional:session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

posts = [
    {
        "id": 1,
        "title": "Penguin",
        "text": "They are a group of aquatic flightless birds"
    },
    {
        "id": 2,
        "title": "Tigers",
        "text": "They are largest living cat species"
    },
    {
        "id": 3,
        "title": "Koalas",
        "text": "They are arboreal herbivorous native to Australia"
    }
]
users = []

# Get posts - for testing
@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World!"}

# Get posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}

# Get single post
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {
            "error": "Post with this ID does not exist"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

# Post a blog post
@app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post: PostSchema, authorization: str = Header(...)):
    # Check the authorization token
    bearer = jwtBearer()
    if not bearer.verify_jwt(authorization):
        raise HTTPException(status_code=401, detail="Invalid token")

    post_id = len(posts) + 1
    post.id = post_id
    posts.append(post.dict())
    return {
        "info": "Post Added!",
        "data": post.dict()
    }

# User Signup
@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    token = signJWT(user.email)
    return {
        "user": user,
        "access_token": token
    }

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

# User Login
@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        token = signJWT(user.email)
        return {
            "user": user,
            "access_token": token
        }
    else:
        return {
            "error": "Invalid Login credentials"
        }

# Verify Token
@app.get("/user/verify-token", tags=["user"])
def verify_token(token: str):
    if token:
        decoded_token = decodeJWT(token)
        if decoded_token:
            return {
                "valid": True,
                "user": decoded_token
            }
    return {
        "valid": False
    }

@app.get("/user/verify-token", tags=['user'])
def verify_token(token: str):
    if token:
        decoded_token = decodeJWT(token)
        if decoded_token:
            return{
                "valid":True,
                "user":decoded_token
            }
    return{
        "valid":False
    }


#if __name__ == "__main__":
    #uvicorn.run(app, host="0.0.0.0", port=8080)
