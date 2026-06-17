import time

def solve_exact_tsp(graph_matrix, hub_index=0):
   
    start_time = time.perf_counter()
    num_nodes = len(graph_matrix)
    
    best_state = {
        'route': [],
        'distance': float('inf')
    }
    
    visited = [False] * num_nodes
    visited[hub_index] = True
    current_route = [hub_index]
    
    _dfs_backtrack(graph_matrix, hub_index, visited, current_route, 0.0, best_state, hub_index)
    
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    
    return best_state['route'], execution_time_ms

def _dfs_backtrack(matrix, current_node, visited, current_route, current_distance, best_state, hub_index):
    num_nodes = len(matrix)
    
    if current_distance >= best_state['distance']:
        return

    if len(current_route) == num_nodes:
        total_distance = current_distance + matrix[current_node][hub_index]
        if total_distance < best_state['distance']:
            best_state['distance'] = total_distance
            best_state['route'] = current_route + [hub_index]
        return
    
    for next_node in range(num_nodes):
        if not visited[next_node]:
            visited[next_node] = True
            current_route.append(next_node)
            
            _dfs_backtrack(
                matrix, next_node, visited, current_route, 
                current_distance + matrix[current_node][next_node], 
                best_state, hub_index
            )
        
            current_route.pop()
            visited[next_node] = False