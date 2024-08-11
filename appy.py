from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/productionplan', methods=['POST'])
def production_plan():
    data = request.get_json()
    
    load = data['load']
    fuels = data['fuels']
    powerplants = data['powerplants']
    
    # Calcular el mérito de cada planta basado en el costo y la eficiencia
    merit_order = sorted(powerplants, key=lambda x: calculate_cost(x, fuels))
    
    # Distribuir la carga entre las plantas
    result = distribute_load(load, merit_order, fuels)
    
    return jsonify(result)

def calculate_cost(plant, fuels):
    if plant['type'] == 'windturbine':
        return 0  # Costo cero para turbinas eólicas
    elif plant['type'] == 'gasfired':
        return fuels['gas(euro/MWh)'] / plant['efficiency'] +0.3*fuels['co2(euro/ton)']
    elif plant['type'] == 'turbojet':
        return fuels['kerosine(euro/MWh)'] / plant['efficiency']

def distribute_load(load, merit_order, fuels):
    production_plan = []
    remaining_load = load
    
    for plant in merit_order:
        if remaining_load <= 0:
            production_plan.append({"name": plant["name"], "p": 0.0})
            continue
        if plant["type"]=='windturbine':
            max_production = min(plant['pmax']*fuels['wind(%)']/100, remaining_load)
        else:
            max_production = min(plant['pmax'], remaining_load)
        if max_production < plant['pmin']:
            production_plan.append({"name": plant["name"], "p": 0.0})
        else:
            production = round(max_production, 1)
            production_plan.append({"name": plant["name"], "p": float(production)})
            remaining_load -= production
    
    return production_plan

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)