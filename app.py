from flask import Flask, render_template, redirect, url_for, request
from src.auth.service import TodoService
from src.auth.models import UserRequest
from uuid import UUID

app = Flask(__name__)

todo_services = TodoService()


@app.route("/")
def index():
    return redirect(url_for("login"))
                


@app.route("/login") #successfully logged in
def login():
    return render_template("login.html")

@app.route("/login_process" ,methods=['POST']) 
def login_process():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        row = todo_services.authenticate_user(username, password)
        if row:
            return redirect(url_for("todo", data=dict(row)))
    
        else:
            return redirect(url_for("login"))

@app.route("/resigter") #redirect to login after successfully registering
def register():
    return render_template("login.html")

@app.route("/resigter_process", methods=['POST'])  #redirect to regiter when the credintials aren't correct
def register_proces():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_process():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        user_data = UserRequest(name=name, email=email, password=password)
        row = todo_services.create_user(user_data)
        if row:
            return redirect(url_for("login"))
        else:
            return redirect(url_for("register"))

@app.route("/todo_get") 
def todo_get(user_id):
    user_id = UUID(user_id)
    todos = todo_services.get_todo(user_id)

    return render_template("todo.html", todos=todos)


@app.route("/todo")
def todo(data):
    return render_template("todo.html", data=data)


@app.route("/todo_update", methods=["POST"])
def todo_update():
    todo_id = request.form["todo_id"]
    title = request.form["title"]
    description = request.form["description"]
    # add update todo function from services
    
    return redirect(url_for("todo_get", user_id=request.form["user_id"]))

@app.route("/sub_todo_get") #get sub_todo
def sub_todo_get(todo_id):
    todo_id = UUID(todo_id)
    subtodos = todo_services.get_sub_todo(todo_id)
    return render_template("sub_todo.html", subtodos=subtodos)



@app.route("/sub_todo", methods=["POST"])
def sub_todo():
    todo_id = request.form.get("todo_id")
    title = request.form.get("title")
    
    return redirect(url_for("update_todo", todo_id=todo_id))


@app.route("/sub_todo_update") #updating todo
def sub_todo_update():
    return redirect(url_for("sub_todo"))

@app.route("/sub_todo_update", methods=["POST"])
def sub_todo_update():
    todo_id = request.form.get("todo_id")
    return redirect(url_for("update_sub_todo", todo_id=todo_id))



if __name__ == "__main__":
    app.run(debug=True)
