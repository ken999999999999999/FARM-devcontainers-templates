import uuid
from bson import ObjectId
from fastapi import Depends, HTTPException,  status, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from apps.dependencies.db import db_context
from apps.models.users.model import User

security = HTTPBearer()


async def db_authorize(token: str, db_context: db_context):
    # Implement your own authentication mechanism
    # user = await db_context.users.find_one({"_id": ObjectId(token)})
    # if (user == None):
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Invalid authentication credentials",
    #         headers={"WWW-Authenticate": "Bearer"}
    #     )

    # return User(**user)

    return User(id=uuid.uuid4(), email="test@test.com", display_name=token)


async def authorize(db_context: db_context, credentials: HTTPAuthorizationCredentials = Security(security)):

    return await db_authorize(credentials.credentials, db_context)
