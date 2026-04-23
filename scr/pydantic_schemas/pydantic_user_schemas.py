from typing import Optional, List
from pydantic import BaseModel, Field, TypeAdapter, field_validator


class User(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(min_length=2, max_length=100, pattern=r"^[a-zA-Z\s]+$")
    email: Optional[str] = Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    gender: Optional[str]
    status: Optional[str]

    @field_validator("gender")
    @classmethod
    def validate_gender(cls, v: str) -> str:
        allowed = ["male", "female"]
        if v not in allowed:
            raise ValueError(f"gender must be one of {allowed}, got {v}")
        return v

    @field_validator("status")
    @classmethod
    def validate_status(cls, v: str) -> str:
        allowed = ["active", "inactive"]
        if v not in allowed:
            raise ValueError(f"status must be one of {allowed}, got {v}")
        return v

UserListAdapter = TypeAdapter(List[User])