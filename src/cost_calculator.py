def calculate_tco(route, graph_matrix, weights, fuel_price, config_data, execution_time_ms):
    """
    Menghitung TCO berdasarkan parameter rasio bensin dinamis dan biaya server dari JSON.
    """
    total_fuel_cost = 0.0
    current_load = sum(weights)
    max_load = sum(weights) if sum(weights) > 0 else 1
    
    ratio_config = config_data['rasio_konsumsi_bensin']
    full_ratio = ratio_config['saat_penuh_liter_per_km']
    empty_ratio = ratio_config['saat_kosong_liter_per_km']
    
    for i in range(len(route) - 1):
        from_node = route[i]
        to_node = route[i+1]
        distance = graph_matrix[from_node][to_node]
        
        load_ratio = current_load / max_load
        fuel_ratio = empty_ratio + (full_ratio - empty_ratio) * load_ratio
        
        fuel_needed = distance * fuel_ratio
        total_fuel_cost += fuel_needed * fuel_price
        
        current_load -= weights[to_node]

    rp_per_ms = config_data['biaya_komputasi']['rp_per_milidetik']
    server_cost = execution_time_ms * rp_per_ms
    
    total_tco = total_fuel_cost + server_cost
    return total_fuel_cost, server_cost, total_tco