from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from pydantic.types import conint
from typing_extensions import Annotated

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True


class UserOut(BaseModel):
    id : int
    email : EmailStr
    class config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id : int
    owner_id : int
    owner : UserOut
    class config:
        orm_mode = True

class PostOut(PostBase):
    Post : Post
    votes : int

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None

class Vote(BaseModel):
    post_id : int
    # dir : Annotated[int, Field(strict=True, le=1)]
    dir : int