from flask import Flask, render_template, redirect, session, url_for, request
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
            return redirect(url_for("todo", data=dict(row["id"])))
        else:
            return redirect(url_for("login"))

@app.route("/register") #redirect to login after successfully registering
def register():
    return render_template("register.html")

@app.route("/register_process", methods=["POST"])
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

@app.route("/todo_get/<user_id>")
def todo_get(user_id):
    sess_user_id = session.get("user_id")
    if not sess_user_id or sess_user_id != user_id:
        return redirect(url_for("login"))
    todos = todo_services.get_todo(UUID(user_id))
    return render_template("todo.html", todos=todos,user_id=user_id,)


@app.route("/todo")
def todo():
    return render_template("todo.html")


@app.route("/todo_update/<user_id>/<todo_id>", methods=["POST"])
def todo_update(user_id, todo_id):
    sess_user_id = session.get("user_id")
    if not sess_user_id or sess_user_id != user_id:
        return redirect(url_for("login"))

    status = request.form.getlist("status")
    if status:
        todo_services.update_todo(UUID(todo_id), status)
    return redirect(url_for("todo_get", user_id=user_id))

@app.route("/sub_todo_get/<user_id>/<todo_id>")
def sub_todo_get(user_id, todo_id):
    sess_user_id = session.get("user_id")
    if not sess_user_id or sess_user_id != user_id:
        return redirect(url_for("login"))

    subtodos = todo_services.get_sub_todo(UUID(todo_id))
    return render_template("sub_todo.html",subtodos=subtodos,user_id=user_id, todo_id=todo_id)


@app.route("/sub_todo/<user_id>", methods=["POST"])
def sub_todo(user_id):
    sess_user_id = session.get("user_id")
    if not sess_user_id or sess_user_id != user_id:
        return redirect(url_for("login"))

    todo_id = request.form["todo_id"]
    title = request.form["title"]
    todo_services.create_sub_todo(todo_id, title)
    return redirect(url_for("sub_todo_get", user_id=user_id, todo_id=todo_id))


@app.route("/sub_todo_update/<user_id>", methods=["POST"])
def sub_todo_update(user_id):
    sess_user_id = session.get("user_id")
    if not sess_user_id or sess_user_id != user_id:
        return redirect(url_for("login"))

    sub_todo_id = UUID(request.form["sub_todo_id"])
    status = request.form.getlist("status")
    todo_id = request.form["todo_id"]
    if status:
        todo_services.update_sub_todo(sub_todo_id, status)
    return redirect(url_for("sub_todo_get", user_id=user_id, todo_id=todo_id))



if __name__ == "__main__":
    app.run(debug=True)
