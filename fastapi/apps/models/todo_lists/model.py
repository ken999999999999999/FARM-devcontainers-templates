
from pydantic import BaseModel,  Field
from apps.models.common import PyObjectId


class TodoList(BaseModel):
    id: PyObjectId = Field(default=None, alias="_id")
    title: str = Field(..., max_length=200)
