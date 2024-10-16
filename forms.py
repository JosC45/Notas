from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField,TimeField,BooleanField,DateField,SubmitField
from wtforms.validators import DataRequired

class Formulario(FlaskForm):
    titulo=StringField('Titulo',validators=[DataRequired()])
    descripcion=TextAreaField('Descripcion',validators=[DataRequired()],description="Agregue la descripcion")
    visto=BooleanField('Visto',validators=[DataRequired()])
    director=StringField('Director',validators=[DataRequired()])
    duracion=TimeField('Duracion',format='%H:%M',validators=[DataRequired()])
    fecha=DateField('Fecha',format='%Y-%m-%D',validators=[DataRequired()])
    prioridad=IntegerField('Prioridad',validators=[DataRequired()])
    submit=SubmitField('Enviar')
