from src.auth.schemas import users, todos, sub_todo
from uuid import UUID
from src.database.execute import DBClient
from src.auth.models import TodoRequest, SubTodoRequest, UserRequest

class TodoQueries:
    def __init__(self):
        self.join_table = users.outerjoin(todos, users.c.id == todos.c.user_id).outerjoin(sub_todo, todos.c.id == sub_todo.c.todo_id)
        self.db_client = DBClient()

    def get_all_todos(self, user_id: UUID, status_type:str):
        query = todos.select().where(todos.c.user_id == user_id)
        row = self.db_client.execute_all(query)
        return row

    def get_sub_todo_by_id(self, todo_id: UUID):
        query = sub_todo.select().where(sub_todo.c.todo_id == todo_id)
        row = self.db_client.execute_all(query)
        return row

    def create_todo(self, todo_data: TodoRequest):
        query = todos.insert().values(dict(todo_data.model_dump(exclude_unset=True))).returning(todos)
        row = self.db_client.execute_one(query)
        return row

    def update_todo(self, todo_id: UUID, status: str):
        query = todos.update().values(status=status).where(todos.c.id == todo_id).returning(todos)
        row = self.db_client.execute_one(query)
        return row

    def create_sub_todo(self, todo_data: SubTodoRequest):
        query = sub_todo.insert().values(dict(todo_data.model_dump(exclude_unset=True))).returning(sub_todo)
        row = self.db_client.execute_one(query)
        return row

    def update_sub_todo(self, todo_id: UUID, status: str):
        query = sub_todo.update().values(status=status).where(sub_todo.c.id == todo_id).returning(sub_todo)
        row = self.db_client.execute_one(query)
        return row

    def create_user(self, user_data: UserRequest):
        query = users.insert().values(dict(user_data.model_dump(exclude_unset=True))).returning(users)
        row = self.db_client.execute_one(query)
        return row

    def get_user(self, user_email: str, user_password: str):
        query = users.select().where(users.c.email == user_email).where(users.c.password == user_password)
        row = self.db_client.execute_one(query)
        return row