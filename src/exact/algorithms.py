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

def solve_greedy_tsp(graph_matrix, hub_index=0):
    start_time = time.perf_counter()

    num_nodes = len(graph_matrix)
    visited = [False] * num_nodes
    visited[hub_index] = True

    route = [hub_index]
    current_node = hub_index

    for _ in range(num_nodes - 1):
        nearest_node = -1
        min_distance = float('inf')

        for next_node in range(num_nodes):
            if not visited[next_node]:
                dist = graph_matrix[current_node][next_node]
                if dist < min_distance:
                    min_distance = dist
                    nearest_node = next_node

        visited[nearest_node] = True
        route.append(nearest_node)
        current_node = nearest_node

    route.append(hub_index)

    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000

    return route, execution_time_ms
