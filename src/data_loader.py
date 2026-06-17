import json
import os

def load_json_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File tidak ditemukan: {file_path}")
    with open(file_path, 'r') as f:
        return json.load(f)

def get_simulation_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    locations_data = load_json_data(os.path.join(base_dir, 'data', 'locations.json'))
    matrix_data = load_json_data(os.path.join(base_dir, 'data', 'distance_matrix.json'))
    scenario_data = load_json_data(os.path.join(base_dir, 'data', 'scenario_config.json'))
    
    weights = [loc['berat_paket_kg'] for loc in locations_data]
    names = [loc['name'] for loc in locations_data]
    matrix = matrix_data['matrix_km']
    
    return matrix, weights, names, scenario_data