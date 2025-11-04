from sqlalchemy import Table, Column, Integer, Text, ForeignKey, DateTime, Enum as SQLEnum
from src.database.connection import metadata
from enum import Enum
from datetime import datetime

class StatusType(Enum):
    deleted='deleted'
    completed='completed'
    in_progress='in-progress'
    pending='pending'    


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", Text, nullable=False),
    Column("email", Text, nullable=False),
    Column("password", Text, nullable=False),
    Column("created_at", DateTime, nullable=False, default=datetime.now()),
    Column("updated_at", DateTime, nullable=True, nupdate=datetime.now())
)

todos = Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column('users_id', ForeignKey("users.id")),
    Column("title", Text, nullable=False),
    Column("description", Text),
    Column("due_date", DateTime),
    Column("status", SQLEnum(StatusType), default=StatusType.pending),
    Column("created_at", DateTime, nullable=False, default=datetime.now()),
    Column("updated_at", DateTime, nullable=True, nupdate=datetime.now())
)

sub_todo = Table(
    "sub_todo",
    metadata,
    Column("id", Integer, primary_key=True),
    Column('todos_id', ForeignKey("todos.id")),
    Column("title", Text, nullable=False),
    Column("description", Text),
    Column("due_date", DateTime),
    Column("status", SQLEnum(StatusType), default=StatusType.pending),
    Column("created_at", DateTime, nullable=False, default=datetime.now()),
    Column("updated_at", DateTime, nullable=True, nupdate=datetime.now())
)
