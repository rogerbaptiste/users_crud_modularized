from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all())

@app.route('/users/new')
def new():
    return render_template("new_user.html")

@app.route('/users/create',methods=['POST'])
def create():
    print(request.form)
    User.create(request.form)
    return redirect('/users')

@app.route('/users/edit/<int:id>')
def edit(id):
    data ={
        'id':id
    }
    return render_template('edit.html',users=User.get_one(data))

@app.route('/users/showuser/<int:id>')
def showuser(id):
    data ={
        "id":id
    }
    return render_template("show.html",users=User.get_one(data))

    #


@app.route('/users/updateuser',methods=['POST'])
def updateuser():
    User.updateuser(request.form)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def delete(id):
    data ={
        'id':id
    }
    User.delete(data)
    return redirect('/users')
