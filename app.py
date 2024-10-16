from flask import Flask,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import Formulario

app=Flask(__name__,template_folder='static/templates')

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:12345@localhost:3306/notas'
#f"mysql+pymysql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = '123'


db=SQLAlchemy(app)
from models import Peliculas,Prioridad
migrate=Migrate(app,db)

@app.route('/ver_peliculas',methods=["GET"])
def listar_peliculas():
    peliculas=Peliculas.query.all()
    if peliculas:
        return jsonify(peliculas),404
    else:
        return jsonify({'error':'usuario no encontrado'}), 404

@app.route('/agregar_pelicula',methods=["POST"])
def agregar_pelicula():
    return

@app.route('/form',methods=['GET'])
def formulario():
    form=Formulario()
    return render_template('agregar.html',form=form)
if __name__=='__main__':
    app.run(Debug=True)

