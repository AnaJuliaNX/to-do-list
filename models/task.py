from app.models import db
# COMO UM MÉTODO CONSTRUTOR
class Task(db.Model):
    __tablename__ = 'taks'

    id = id.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    def __init__(self, title):
        self.title = title

    def to_dict(self):
        return {'id': self.id, 'title': self.title}
   
    @classmethod
    def create(cls, title):
        new_task = cls(title=title)
        db.session.add(new_task)
        db.session.commit
        return new_task

    @classmethod
    def update(cls, title, task_id):
        task = cls.query.get(task_id)
        if task:
            task.title = title
            db.session.commit()
        return task 
    
    @classmethod
    def delete(cls, task_id):
        task = cls.query.get(task_id)
        if task: 
            db.session.delete(task)
            db.session.commit()
        return task  