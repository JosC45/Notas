from app import db

class Peliculas(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(40),nullable=False)
    descripcion=db.Column(db.String(150),nullable=False)
    director=db.Column(db.String(40),nullable=False)
    duracion=db.Column(db.Time,nullable=False)
    estreno=db.Column(db.Date,nullable=False)
    visto=db.Column(db.Boolean,nullable=False)
    prioridad=db.Column(db.Integer,autoincrement=True,unique=True)

    def __init__(self,nombre,descripcion,director,duracion,estreno,visto):
        self.nombre=nombre
        self.descripcion=descripcion
        self.director=director
        self.duracion=duracion
        self.estreno=estreno
        self.visto=visto
        self.prioridad=Peliculas.autoincremento()

    @staticmethod
    def autoincremento():
        max_val=db.session.query(db.func.max(Peliculas.prioridad)).scalar()
        return (max_val or 0)+1



