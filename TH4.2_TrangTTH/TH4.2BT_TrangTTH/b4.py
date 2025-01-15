import os

# Đường dẫn file
file_path = 'C:\\Users\\TV\\Documents\\BTTH_Python\\TH4.2_TrangTTH\\TH4.2BT_TrangTTH\\diem2A.txt'

# Kiểm tra file tồn tại
if not os.path.exists(file_path):
    print(f"Lỗi: Không tìm thấy file {file_path}")
else:
    # Đọc dữ liệu từ file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Kiểm tra file rỗng
    if not lines:
        print("Lỗi: File trống, không có dữ liệu để xử lý.")
    else:
        # Xử lý dữ liệu
        header = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]

        # Tính điểm trung bình của từng học sinh
        def calculate_average_scores(data):
            scores = []
            for row in data:
                if len(row) < 4:  # Đảm bảo đủ dữ liệu (Tên + ít nhất 3 môn)
                    print(f"Dòng dữ liệu không hợp lệ, bị bỏ qua: {row}")
                    continue
                name = row[0]
                try:
                    subjects = list(map(float, row[1:]))
                    avg = sum(subjects) / len(subjects)
                    scores.append((name, avg))
                except ValueError:
                    print(f"Dữ liệu không hợp lệ cho học sinh {row[0]}, bị bỏ qua.")
            return scores

        # Tìm học sinh có điểm trung bình cao nhất và thấp nhất
        def find_extremes(scores):
            max_student = max(scores, key=lambda x: x[1])
            min_student = min(scores, key=lambda x: x[1])
            return max_student, min_student

        # Tính toán
        scores = calculate_average_scores(data)
        if scores:  # Kiểm tra nếu có dữ liệu hợp lệ
            max_student, min_student = find_extremes(scores)

            # In kết quả
            print("\nĐTB của từng học sinh:")
            for name, avg in scores:
                print(f"{name}: {avg:.2f}")

            print(f"\nHọc sinh có điểm TB cao nhất: {max_student[0]} ({max_student[1]:.2f})")
            print(f"Học sinh có điểm TB thấp nhất: {min_student[0]} ({min_student[1]:.2f})")
        else:
            print("Không có dữ liệu hợp lệ để tính toán.")
