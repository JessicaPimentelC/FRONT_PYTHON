from flask import Flask, render_template, request

app = Flask(__name__)

#n_equipos = 0
#distances = [[0] * n_equipos for _ in range(n_equipos)]  # Arreglo bidimensional para almacenar las distancias

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        num_teams = int(request.form['num_teams'])
        #num_teams = request.form.get("equipos", False)
        
        # Obtener las distancias ingresadas en el formulario
        distances = []
        for i in range(num_teams):
            row = []
            for j in range(num_teams):
                if i == j:
                    row.append(0)
                else:
                    print("holaAAA")
                    distance = request.form.get(f'distance_{i}_{j}')
                    if distance is not None:
                        print("if")
                        distance = float(distance)
                    else:
                        distance = 0.0  # Valor predeterminado cuando el campo está vacío
                    row.append(distance)
            distances.append(row)
            print(distances)
        
        return 'Distancias almacenadas correctamente.'
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
