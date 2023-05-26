from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = 'your_secret_key'

BaseModelForm = model_form_factory(FlaskForm)

class DistanceForm(BaseModelForm):
    num_teams = IntegerField('Número de equipos', validators=[DataRequired()])

    class Meta:
        model = None  # Se establecerá dinámicamente más adelante

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DistanceForm(request.form)

    if request.method == 'POST' and form.validate():
        num_teams = form.num_teams.data
        class Distance:
            pass
        n = 0
        DistanceForm.Meta.model = Distance
        for k in range(num_teams):
            n += k
        
        for i in range(n):
            
            field_name = f'distance_{i}'
            field = FloatField(f'Distancia {i+1}', validators=[DataRequired()])
            setattr(DistanceForm, field_name, field)

        form = DistanceForm(request.form)

        if form.validate_on_submit():
            distances = []
            for i in range(n):#n=6 para 4 equipos
                row = []
                if i == 0:
                    row.append(0)
                else:
                    field_name = f'distance_{i}'
                    distance = form.data[field_name]
                    print("distance",distance)
                    row.append(distance)
                    
                distances.append(row)
                print("row",row)
                print("distances:",distances)

            return 'Distancias almacenadas correctamente.'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
