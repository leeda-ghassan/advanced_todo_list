from uuid import UUID
from src.auth.models import TodoRequest, SubTodoRequest, UserRequest
from src.auth.query import TodoQueries


class TodoService:
    def __init__(self):
        self.todo_queries = TodoQueries()

    def create_user(self, user_data: UserRequest):
        user = self.todo_queries.create_user(user_data)
        if not user: 
            raise Exception("login process failed") 
            
        return user
    
    def authenticate_user(self, email: str, password: str):
        user = self.todo_queries.get_user(email, password)
        if not user:
            raise ValueError("invalid credentials")
        return user
    
    def create_todo(self, todo_data: TodoRequest):
        todo = self.todo_queries.create_todo(todo_data)
        if not todo: 
            raise Exception("create todo failed") 
            
        return todo
    
   
    def get_todo(self, user_id: UUID):
        todos = self.todo_queries.get_all_todos(user_id)
        if not todos: 
            raise Exception("create todo failed") 
            
        return todos
    
    def update_todo(self, todo_id: UUID, status: str):
        todo = self.todo_queries.update_todo(todo_id, status)
        if not todo: 
            raise Exception("create todo failed") 
            
        return todo

    def create_sub_todo(self, sub_todo_data: SubTodoRequest):
        sub_todo = self.todo_queries.create_sub_todo(sub_todo_data)

        if not sub_todo: 
            raise Exception("create sub_todo failed") 
            
        return sub_todo
    
    def get_sub_todo(self, todo_id: UUID):
        sub_todos = self.todo_queries.get_sub_todo_by_id(todo_id)
        if not sub_todos: 
            raise Exception("failed to fetch todos") 
            
        return sub_todos

    def update_sub_todo(self, todo_id: UUID, status: str):
        todo = self.todo_queries.update_sub_todo(todo_id, status)
        if not todo: 
            raise Exception("create todo failed") 
            
        return todo

