from flask import Flask,jsonify,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import Formulario

app=Flask(__name__,template_folder='static/templates')

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:12345@localhost:3306/notas'
#f"mysql+pymysql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = '123'


db=SQLAlchemy(app)
from models import Peliculas
migrate=Migrate(app,db)

@app.route('/ver_peliculas/<filterr>',methods=["GET"])
def listar_peliculas(filterr):
    print(filterr)
    if filterr:
        if filterr=="id":
            pelis=Peliculas.query.order_by(Peliculas.id).all()
            return render_template("listar.html",peliculas=pelis)
        if filterr=="prioridad":
            pelis=Peliculas.query.order_by(Peliculas.prioridad).all()
            return render_template("listar.html",peliculas=pelis)
        if filterr=="año":
            pelis=Peliculas.query.order_by(Peliculas.estreno).all()
            return render_template("listar.html",peliculas=pelis)  
        else:
            peliculas=Peliculas.query.order_by(Peliculas.prioridad).all()
    # for pelis in peliculas:
    #     pel.append({
    #         'id':pelis.id,
    #         'titulo':pelis.nombre,
    #         'descripcion':pelis.descripcion,
    #         'director':pelis.director,
    #         'duracion':pelis.duracion.strftime("%H:%M"),
    #         'estreno':pelis.estreno,
    #         'visto':pelis.visto,
    #         'prioridad':pelis.prioridad,
    #     })
    # if peliculas:
    #     print(pel)
    #     return jsonify(pel),101
            if peliculas:
                return render_template('listar.html',peliculas=peliculas)
            else:
                return jsonify({'error':'usuario no encontrado'}), 404

@app.route('/agregar_pelicula',methods=["POST"])
def agregar_pelicula():
    
    return

@app.route('/form',methods=['GET','POST'])
def formulario():
    form=Formulario()
    if form.validate_on_submit():
        titulo=form.titulo.data
        print(titulo)
        visto=form.visto.data
        print(visto)
        descripcion=form.descripcion.data
        print(descripcion)
        director=form.director.data
        print(director)
        duracion=form.duracion.data
        print(duracion)
        duracion_str=duracion.strftime("%H:%M")
        fecha=form.fecha.data
        print(fecha)
        #prioridad=form.prioridad.data
        new_film=Peliculas(nombre=titulo,descripcion=descripcion,visto=visto,estreno=fecha,director=director,duracion=duracion)
        print(new_film)
        db.session.add(new_film)
        db.session.commit()
        return jsonify({"Pelicula":{"titulo":titulo,"descripcion":descripcion,"visto":visto,"director":director,"duracion":duracion_str,"fecha":fecha}})
    else:
        print(form.errors)
        return render_template('agregar.html',form=form)
    
@app.route("/editar_pelicula/<int:id_ed>",methods=['POST','PUT'])
def editar(id_ed):
    form=Formulario()
    pelicula=Peliculas.query.filter_by(id=id_ed).first()
    fecha_formateada=pelicula.estreno.strftime("%d-%m-%Y") if pelicula.estreno else None
    if form.validate_on_submit():
        pelicula.titulo=form.titulo.data
        pelicula.descripcion=form.descripcion.data
        pelicula.visto=form.visto.data
        pelicula.director=form.director.data
        pelicula.duracion=form.duracion.data
        pelicula.fecha=form.fecha.data

        db.session.commit()
        return jsonify({"Pelicula":{"titulo":form.titulo.data,"descripcion":form.descripcion.data,"visto":form.visto.data,"director":form.director.data,"duracion":form.duracion,"fecha":form.fecha.data}})
    else:
        print(form.errors)
        return render_template('editar.html',pelicula=pelicula,fecha=fecha_formateada,form=form)

@app.route("/eliminar_pelicula/<int:id_ed>",methods=["POST"])
def eliminar(id_ed):
    pelicula=Peliculas.query.filter_by(id=id_ed).first()
    if pelicula:
        db.session.delete(pelicula)
        db.session.commit()
        return jsonify({"mensaje":"Pelicula eliminada"})
    return jsonify({"mensaje":"pelicula no encontrada"})




if __name__=='__main__':
    app.run(Debug=True)


