from collections import deque

class State:
    def __init__(self, jug3, jug8, jug12):
        self.jugs = [jug3, jug8, jug12]
        self.capacities = [3, 8, 12]
    def __eq__(self, other):
        return self.jugs == other.jugs
    def __hash__(self):
        return hash(tuple(self.jugs))

def get_next_states(state):
    next_states = []
    
    # Đổ nước từ can này sang can khác
    for i in range(3):
        for j in range(3):
            if i != j:
                # Tính xem có thể đổ bao nhiêu nước vào can 
                amount = min(state.jugs[i], state.capacities[j] - state.jugs[j])
                if amount > 0:
                    new_jugs = state.jugs.copy()
                    new_jugs[i] -= amount
                    new_jugs[j] += amount
                    next_states.append(State(*new_jugs))
    
    # Đổ đầy nước vào 1 can 
    for i in range(3):
        if state.jugs[i] < state.capacities[i]:
            new_jugs = state.jugs.copy()
            new_jugs[i] = state.capacities[i]
            next_states.append(State(*new_jugs))
    
    # Đổ hết nước trong can 
    for i in range(3):
        if state.jugs[i] > 0:
            new_jugs = state.jugs.copy()
            new_jugs[i] = 0
            next_states.append(State(*new_jugs))
    
    return next_states

def solve_water_jug():
    initial_state = State(0, 0, 0) # trạng thái ban đầu : cả 3 can không có nước 
    target = 1  # Trạng thái đích: Nước trong 1 can là 1 lít 
    
    queue = deque([(initial_state, [])])
    visited = {initial_state}
    
    while queue:
        current_state, path = queue.popleft()
        
        # Kiểm tra xem nước trong can đã là 1 lít chưa 
        if target in current_state.jugs:
            return path + [current_state]
        
        # Tạo và xử lý các trạng thái tiếp 
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))
    
    return None

# Chạy và in kết quả
solution = solve_water_jug()
if solution:
    print("Tìm thấy lời giải:")
    for i, state in enumerate(solution):
        print(f"Bước {i}: Can 3L: {state.jugs[0]}L, Can 8L: {state.jugs[1]}L, Can 12L: {state.jugs[2]}L")
else:
    print("Không tìm thấy lời giải")