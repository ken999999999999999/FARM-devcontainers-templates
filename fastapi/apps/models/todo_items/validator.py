from bson import ObjectId
from fastapi import Body
from fastapi.exceptions import RequestValidationError
from apps.dependencies.db import db_context
from apps.models.todo_items.dto import CreateTodoItemCommand


async def create_todo_item_validator(db_context: db_context, command: CreateTodoItemCommand = Body(...)):

    if await db_context.todo_lists.find_one({"_id": ObjectId(command.todo_list_id)}) != None:
        raise RequestValidationError(errors=["Todo List is not exist"])

    return
