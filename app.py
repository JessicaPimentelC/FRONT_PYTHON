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
    maximo = IntegerField('Valor Maximo')
    minimo = IntegerField('Valor Minimo')

    class Meta:
        model = None  # Se establecerá dinámicamente más adelante

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DistanceForm(request.form)

    if request.method == 'POST' and form.validate():
        num_teams = form.num_teams.data
        maximo = form.maximo.data
        minimo = form.minimo.data
        
        class Distance:
            pass
        n = 0
        DistanceForm.Meta.model = Distance
        for k in range(num_teams):
            n += k
        
        for i in range(n):
            field_name = f'distance_{i+1}'
            field = IntegerField(f'Distancia {i+1}', validators=[DataRequired()])
            setattr(DistanceForm, field_name, field)

        form = DistanceForm(request.form)
        filasDist = []
        filasEntra = []
        matriz = []
        if form.validate_on_submit():
            entrada = []
            for i in range(n):#ej: n_campos=6 para 4 equipos
                row = []
                if i == 0:
                    row.append(0)
                else:                    
                    field_name = f'distance_{i}'
                    distance = form.data[field_name]
                    row.append(distance) 
            
                entrada.append(row)              
            
            #datos de entrada, distancias entre equipos
            for i in range(n):
                filasDist.append(entrada[i][0])
            
            #datos de entrada, num equipos, maximo y minimo    
            filasEntra.append(num_teams)
            filasEntra.append(maximo)
            filasEntra.append(minimo)
            
            matrix = []

            for i in range(num_teams):
                r = []
                for j in range(num_teams):
                    if i == j:
                        r.append(0)
                    elif i < j:
                        r.append(filasDist.pop(0))
                    else:
                        r.append(matrix[j][i])
                matrix.append(r)

            result = '[' + ']['.join([' '.join(map(str, row)) for row in matrix]) + ']'
            result = result.replace('[', '[').replace(']', ']')

            print(result)


            
            return 'Distancias almacenadas correctamente.'
        
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
