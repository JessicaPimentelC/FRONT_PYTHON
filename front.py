from flask import Flask, render_template, request

app = Flask(__name__)

#n_equipos = 0
#distances = [[0] * n_equipos for _ in range(n_equipos)]  # Arreglo bidimensional para almacenar las distancias

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_teams = int(request.form['num_teams'])
        distances = []
        for i in range(num_teams):
            row = []
            for j in range(num_teams):
                if i == j:
                    row.append(0)
                else:
                    distance = request.form.get(f'distance_{i}_{j}')
                    if distance:
                        row.append(float(distance))
                    else:
                        row.append(0.0)
            distances.append(row)

        return 'Distancias almacenadas correctamente.'

    return render_template('index.html', num_teams=2) 


if __name__ == '__main__':
    app.run(debug=True)
