from app import db

class Peliculas(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(40),nullable=False)
    director=db.Column(db.String(40),nullable=False)
    duracion=db.Column(db.Time,nullable=False)
    estreno=db.Column(db.Date,nullable=False)
    visto=db.Column(db.Boolean,nullable=False)

    prioridad=db.relationship('Prioridad',backref='peliculas',uselist=False,cascade="all,delete-orphan")

class Prioridad(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    id_pelicula=db.Column(db.Integer,db.ForeignKey('peliculas.id'), )

