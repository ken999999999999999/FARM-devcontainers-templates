from http.client import BAD_REQUEST
from bson import ObjectId
from fastapi import APIRouter, Body, Depends, HTTPException
from apps.dependencies.auth import authorize
from apps.dependencies.db import db_context
from apps.models.todo_items.dto import CreateTodoItemCommand, UpdateTodoItemCommand
from apps.models.todo_items.model import TodoItem
from apps.models.todo_items.validator import create_todo_item_validator


router = APIRouter(
    prefix="/todo-items",
    tags=["todo-items"],
    dependencies=[Depends(authorize)]
)


@router.post("/", dependencies=[Depends(create_todo_item_validator)])
async def create_todo_item_command(db_context: db_context, command: CreateTodoItemCommand = Body(...)) -> str:

    newItem = TodoItem(**command.model_dump())

    return str((await db_context.todo_items.insert_one(newItem.model_dump(exclude=["id"]))).inserted_id)


@router.put("/{id}")
async def update_todo_item_command(db_context: db_context, id: str, command: UpdateTodoItemCommand = Body(...)) -> None:

    if id != command.id:
        return BAD_REQUEST()

    if (await db_context.todo_items.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"is_done": command.is_done}})) == None:
        raise HTTPException(
            status_code=404, detail=f"Todo Item {id} not found")
    return
