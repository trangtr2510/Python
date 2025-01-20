from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

def create_test_graph():
    g = Graph()
    # Thêm các cạnh từ đồ thị
    g.add_edge('START', 'd', 3)
    g.add_edge('START', 'p', 1)
    g.add_edge('START', 'e', 9)
    g.add_edge('p', 'q', 1)
    g.add_edge('p', 'h', 4)
    g.add_edge('q', 'r', 3)
    g.add_edge('q', 'h', 4)
    g.add_edge('h', 'r', 3)
    g.add_edge('d', 'b', 1)
    g.add_edge('d', 'c', 8)
    g.add_edge('d', 'e', 2)
    g.add_edge('b', 'a', 2)
    g.add_edge('a', 'c', 2)
    g.add_edge('f', 'c', 5)
    g.add_edge('e', 'r', 9)
    g.add_edge('r', 'f', 5)
    g.add_edge('f', 'GOAL', 5)
    return g

def bfs(graph, start, goal):
    """Tìm kiếm theo chiều rộng"""
    queue = deque([(start, [start], 0)])
    visited = {start}
    
    while queue:
        vertex, path, cost = queue.popleft()
        if vertex == goal:
            return path, cost
            
        for next_vertex, weight in graph.graph[vertex]:
            if next_vertex not in visited:
                visited.add(next_vertex)
                queue.append((next_vertex, path + [next_vertex], cost + weight))
    return None, float('inf')

def dfs(graph, start, goal):
    """Tìm kiếm theo chiều sâu"""
    stack = [(start, [start], 0)]
    visited = {start}
    
    while stack:
        vertex, path, cost = stack.pop()
        if vertex == goal:
            return path, cost
            
        for next_vertex, weight in reversed(graph.graph[vertex]):
            if next_vertex not in visited:
                visited.add(next_vertex)
                stack.append((next_vertex, path + [next_vertex], cost + weight))
    return None, float('inf')

def uniform_cost_search(graph, start, goal):
    """Tìm kiếm theo giá thấp nhất"""
    priority_queue = [(0, start, [start])]
    visited = set()
    
    while priority_queue:
        cost, vertex, path = heapq.heappop(priority_queue)
        
        if vertex == goal:
            return path, cost
            
        if vertex not in visited:
            visited.add(vertex)
            
            for next_vertex, weight in graph.graph[vertex]:
                if next_vertex not in visited:
                    heapq.heappush(priority_queue, 
                                 (cost + weight, next_vertex, path + [next_vertex]))
    return None, float('inf')

def iterative_deepening(graph, start, goal):
    """Tìm kiếm sâu lặp"""
    def dfs_limited(vertex, goal, depth, path, cost, visited):
        if depth == 0 and vertex != goal:
            return None, float('inf')
        if vertex == goal:
            return path, cost
            
        visited.add(vertex)
        for next_vertex, weight in graph.graph[vertex]:
            if next_vertex not in visited:
                result, new_cost = dfs_limited(next_vertex, goal, depth - 1, 
                                             path + [next_vertex], cost + weight, visited.copy())
                if result:
                    return result, new_cost
        return None, float('inf')

    max_depth = 20  # Giới hạn độ sâu tối đa
    for depth in range(max_depth):
        result, cost = dfs_limited(start, goal, depth, [start], 0, set())
        if result:
            return result, cost
    return None, float('inf')

# Tạo đồ thị và chạy các thuật toán
graph = create_test_graph()

print("1. Tìm kiếm theo chiều rộng (BFS):")
path, cost = bfs(graph, 'START', 'GOAL')
print(f"Đường đi: {' -> '.join(path)}")
print(f"Chi phí: {cost}\n")

print("2. Tìm kiếm theo chiều sâu (DFS):")
path, cost = dfs(graph, 'START', 'GOAL')
print(f"Đường đi: {' -> '.join(path)}")
print(f"Chi phí: {cost}\n")

print("3. Tìm kiếm theo giá thấp nhất:")
path, cost = uniform_cost_search(graph, 'START', 'GOAL')
print(f"Đường đi: {' -> '.join(path)}")
print(f"Chi phí: {cost}\n")

print("4. Tìm kiếm sâu lặp:")
path, cost = iterative_deepening(graph, 'START', 'GOAL')
print(f"Đường đi: {' -> '.join(path)}")
print(f"Chi phí: {cost}")