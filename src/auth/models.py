from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class TodoRequest(BaseModel):
    user_id: UUID
    title: str
    description: str
    due_date: datetime
    status: str

class SubTodoRequest(BaseModel):
    todo_id: UUID
    title: str
    description: str
    due_date: datetime
    status: str

class UserRequest(BaseModel):
    name: str
    email: str
    password: str

class TodoResponse(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    description: str
    due_date: datetime
    status: str

class SubTodoResponse(BaseModel):
    id: UUID
    todo_id: UUID
    title: str
    description: str
    due_date: datetime
    status: str

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str
    password: str