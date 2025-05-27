from flask import Blueprint, render_template, request, redirect, url_for
from app.models.task import Task
from app import db

# Blueprint
task_bp =  Blueprint('task_bp', __name__)

# construindo a minha rota 
@task_bp.route('/tasks', methods=['GET'])
def list_tasks(): 
    tasks = Task.query.all()
    return render_template('task_list.html', tasks=tasks)

@task_bp.route('/tasks/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']

        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit
        return redirect(url_for('task_bp_list_tasks'))
    return render_template('create_task.html') 

@task_bp.route('task/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form['title']
        db.session.commit()
        return redirect(url_for('task_bp.list_tasks'))
    return render_template('update_task.html', task=task)


@task_bp.route('/delete/<int:task_id>', method=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('task_bp.list_tasks'))

