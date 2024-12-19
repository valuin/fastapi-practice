from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserModel(BaseModel):
    name: str
    email: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime


