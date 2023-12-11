from http.client import BAD_REQUEST
from bson import ObjectId
from fastapi import APIRouter, Body, Depends, HTTPException
from apps.dependencies.auth import authorize
from apps.dependencies.db import db_context
from apps.models.todo_lists.dto import CreateTodoListCommand, TodoListDto, UpdateTodoListCommand
from apps.models.todo_lists.model import TodoList


router = APIRouter(
    prefix="/todo-lists",
    tags=["todo-lists"],
    dependencies=[Depends(authorize)]
)


@router.get("/list/")
async def get_todo_lists_command(db_context: db_context,) -> [TodoListDto]:
    query = await db_context.todo_lists.aggregate([
        {"$lookup": {
            "from": "todo_items",
            "let": {"todo_list_object_id": {"$toObjectId": "$todo_list_id"}},
            "pipeline": [
                {"$match": {
                    "$expr": {"$eq": ["$_id", "$$todo_list_object_id"]}}},
                {"$addFields": {"id": {"$toString": "$_id"}}}
            ],
            "as": "todo_items"
        }},
        {"$addFields": {
            "id": {"$toString": "$_id"}
        }}
    ]).to_list(None)

    return [TodoListDto(**record) for record in query]


@router.post("/")
async def create_todo_list_command(db_context: db_context, command: CreateTodoListCommand = Body(...)) -> str:

    newList = TodoList(**command.model_dump())

    return str((await db_context.todo_lists.insert_one(newList.model_dump(exclude=["id"]))).inserted_id)


@router.put("/{id}")
async def update_todo_list_command(db_context: db_context, id: str, command: UpdateTodoListCommand = Body(...)) -> None:

    if id != command.id:
        return BAD_REQUEST()

    if (await db_context.todo_lists.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"title": command.title}})) == None:
        raise HTTPException(
            status_code=404, detail=f"Todo List {id} not found")
    return
