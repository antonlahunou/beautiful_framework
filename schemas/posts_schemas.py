from typing import Optional, List
from pydantic import BaseModel, Field, TypeAdapter, field_validator


class Post(BaseModel):
    id: int = Field(ge=0)
    post_id: int = Field(ge=0)
    name: str = Field(min_length=2, max_length=100, pattern=r"^[a-zA-Z\.\s]+$")
    email: Optional[str] = Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    body: str = Field(min_length=1, max_length=1000, pattern=r"^[a-zA-Z\.\s]+$")

UserListAdapter = TypeAdapter(List[Post])

class CreatePostRequest(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    body: str