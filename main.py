from datetime import datetime
from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from config import CONFIG

db = SQLAlchemy() #ORM (Object-Relacional mapping)
ma = Marshmallow() #Serializar los datos

def create_app(): 
    '''Application-factory pattern'''
    app = Flask(__name__)
    app.config.from_object(CONFIG)

    CORS(app) 
    db.init_app(app) #ORM
    Migrate(app, db) #Migraciones de la db
    ma.init_app(app) #Serializer data

    return app

#Instanción de la aplicación
app = create_app()


#Modelo de datos BD
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(250), nullable = True)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow(), onupdate = datetime.utcnow())

    def __repr__(self):
        '''Represenctacion del objeto, para visualizarlo por consola
        '''
        return f'{self.title}'

    def __init__(self, title, description):
        '''Constructor de la clase'''
        self.title = title
        self.description = description


#Esquema para serializar los datos
class TaskSchema(ma.Schema): 
    class Meta: 
        # Fields to expose
        fields = ('id', 'title', 'description', 'updated_at')


task_schema = TaskSchema() #Esquema para una sola tarea
tasks_schema = TaskSchema(many= True) #Esquema para multiples tareas


#Rutas
@app.route("/tasks", methods = ["GET", "POST"])
def add_tasks(): 
    ''' Listar o Registro Tasks
    '''
    if request.method == "GET":
        #Todas las tasks registradas, ordenadas por ID
        tasks = Task.query.order_by(Task.id).all()
        return tasks_schema.jsonify(tasks)

    elif request.method == "POST":
        #Creación de una nueva tasks
        data = request.json 
        nueva_empresa = Task(title = data.get("title"), description = data.get("description"))
        db.session.add(nueva_empresa)
        db.session.commit()

        return {"message": "Creado con exito"}, 200



@app.route("/tasks/<int:id>", methods = ["GET", "PUT", "DELETE"])
def tasks_view(id): 
    ''' Consultar, Actualizar o Eliminar una tarea, por ID
    '''
    tasks = Task.query.get_or_404(id)

    if request.method == "GET":
        # Consultar una Task
        return task_schema.jsonify(tasks), 200

    elif request.method == "PUT":
        # Actualizar el objeto 

        data = request.json 
        tasks.title = data.get('title')
        tasks.description = data.get('description')
        db.session.commit()

        return {"message": "Actualizado con exito"}, 202
    
    elif request.method == "DELETE": 
        #Eliminar de forma permanente una Tasks
        db.session.delete(tasks)
        db.session.commit()

        return {"message": f"Eliminada la Tasks con id: {id}"}, 200



if __name__ == "__main__": 
    app.run()


