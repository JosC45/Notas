from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField,TimeField,BooleanField,DateField,SubmitField
from wtforms.validators import DataRequired

class Formulario(FlaskForm):
    titulo=StringField('Titulo',validators=[DataRequired()])
    descripcion=TextAreaField('Descripcion',validators=[DataRequired()])
    visto=BooleanField('Visto')
    director=StringField('Director',validators=[DataRequired()])
    duracion=TimeField('Duracion',format='%H:%M:%S')
    fecha=DateField('Fecha',format='%d-%m-%Y')
    submit=SubmitField('Enviar')
