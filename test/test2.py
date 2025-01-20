from collections import deque

class State:
    def __init__(self, x, y, z):
        # x: Số nhà truyền giáo ở trên một bờ sông.
        # y: Số người ăn thịt ở trên một bờ sông
        # z: Vị trí thuyền (1 nếu ở bờ trái, 0 nếu ở bờ phải).

        self.x = x
        self.y = y
        self.z = z

        # Số lượng người ở bờ phải
        # x1: Số nhà truyền giáo ở bờ bên kia .
        # y1: Số người ăn thịt ở bờ bên kia .
        self.x1 = 3 - x
        self.y1 = 3 - y

    def is_valid(self):
        # Kiểm tra xem trạng thái có hợp lệ không.
        # return: True nếu hợp lệ, ngược lại False.
        
        # Kiểm tra số lượng người hợp lệ
        if (self.x < 0 or self.x1 < 0 or
            self.y < 0 or self.y1 < 0):
            return False

        # Kiểm tra số người ăn thịt không vượt số nhà truyền giáo trên bờ hoặc trên thuyền 
        if (self.x > 0 and self.x < self.y) or \
           (self.x1 > 0 and self.x1 < self.y1):
            return False

        return True

# Dùng để so sánh xem hai trạng thái có bằng nhau hay không.
    def __eq__(self, other):
        return (self.x == other.x and
                self.y == other.y and
                self.z == other.z)
# Dùng để tạo giá trị băm duy nhất cho một trạng thái.
    def __hash__(self):
        return hash((self.x, self.y, self.z))

def get_next_states(state):
    # Sinh các trạng thái tiếp theo từ trạng thái hiện tại.
    # state: Trạng thái hiện tại.
    # return: Danh sách các trạng thái hợp lệ tiếp theo.
    
    next_states = []
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Các cách di chuyển hợp lệ

    for m, c in moves:
        if state.z:  # Thuyền từ trái sang phải
            new_state = State(
                state.x - m,
                state.y - c,
                0
            )
        else:  # Thuyền từ phải sang trái
            new_state = State(
                state.x + m,
                state.y + c,
                1
            )

        if new_state.is_valid():
            next_states.append(new_state)

    return next_states

def solve_missionaries_cannibals():
    
    # return: Danh sách các trạng thái từ trạng thái đầu đến trạng thái đích.
    
    initial_state = State(0, 0, 0)  # Trạng thái ban đầu: tất cả ở trên 1 bờ 
    goal_state = State(3, 3, 1)     # Trạng thái đích: tất cả ở bờ bên kia 

    queue = deque([(initial_state, [])])  # Hàng đợi BFS
    visited = {initial_state}            # Bộ lưu các trạng thái đã duyệt

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]  # Trả về đường đi nếu tìm thấy lời giải

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

    return None  # Không tìm thấy lời giải

# Chạy và in kết quả
solution = solve_missionaries_cannibals()
if solution:
    print("Tìm thấy lời giải:")
    for i, state in enumerate(solution):
        print(f"Bước {i}:")
        print(f"Bờ trái: {state.x} nhà truyền giáo - {state.y} người ăn thịt")
        print(f"Bờ phải: {state.x1} nhà truyền giáo - {state.y1} người ăn thịt")
        print(f"Thuyền ở bờ: {'trái' if state.z else 'phải'}\n")
else:
    print("Không tìm thấy lời giải")
