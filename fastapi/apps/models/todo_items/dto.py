from datetime import datetime
from pydantic import BaseModel, Field
from apps.models.common import PyObjectId


class CreateTodoItemCommand(BaseModel):
    title: str = Field(..., max_length=200)
    todo_list_id: PyObjectId


class UpdateTodoItemCommand(BaseModel):
    id: PyObjectId
    is_done: bool


class TodoItemDto(BaseModel):
    id: PyObjectId
    title: str = Field(..., max_length=200)
    is_done: bool = Field(default=False)
    created_on: datetime
