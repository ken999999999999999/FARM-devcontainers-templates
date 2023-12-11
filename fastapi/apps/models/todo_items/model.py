
from datetime import datetime
from pydantic import BaseModel,  Field
from apps.models.common import PyObjectId


class TodoItem(BaseModel):
    id: PyObjectId = Field(default=None, alias="_id")
    title: str = Field(..., max_length=200)
    is_done: bool = Field(default=False)
    created_on: datetime = Field(default_factory=datetime.now)
    todo_list_id: PyObjectId = Field(...)
