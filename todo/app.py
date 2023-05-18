from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): #string representation of our model
        return f'{id}'


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':# when you need to insert a new todo ---> CREATE
        task_content = request.form['content'] #dict
        new_task = Todo(content=task_content) #object of the model Todo

        try: #async operations
            db.session.add(new_task) #SQL INSERT
            db.session.commit()
            return redirect("/")#to render the new todo as well as the previous todos
        except:
            return "There was an issue adding your task"
    else: # when you need to fetch all todos ---> READ
        tasks = Todo.query.order_by(Todo.date_created).all()#fetching all the todos from the database and arranging them in ascending order
        return render_template('index.html', tasks=tasks)
    
@app.route("/delete/<int:id>")
def delete(id): #--> DELETE
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "There was a problem deleting the task"
    
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue updating your task"
    else:
        return render_template('update.html', task=task)
    
@app.route("/getcomments")
def getComments():
    response = requests.get('https://jsonplaceholder.typicode.com/comments') #Response object
    resonseJson = response.json()
    return render_template('comments.html', comments=resonseJson)

if __name__ == '__main__':
    app.run(debug=True)


# 1. GIT and GITHUB 
