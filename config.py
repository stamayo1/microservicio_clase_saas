import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class CONFIG: 
    ''' Configuración de variables de entorno para la 
    instanciación de la aplicación
    '''
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite' #Base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False