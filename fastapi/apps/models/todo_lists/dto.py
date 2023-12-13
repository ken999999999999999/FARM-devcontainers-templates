from pydantic import BaseModel, Field
from apps.models.common import PyObjectId
from apps.models.todo_items.dto import TodoItemDto


class CreateTodoListCommand(BaseModel):
    title: str = Field(..., max_length=200)


class UpdateTodoListCommand(BaseModel):
    id: PyObjectId
    title: bool


class TodoListDto(BaseModel):
    id: PyObjectId
    title: str = Field(..., max_length=200)
    todo_items: list[TodoItemDto]