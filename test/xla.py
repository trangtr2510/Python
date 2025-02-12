import cv2
import torch
from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load mô hình YOLOv8 pre-trained
model = YOLO("yolov8n.pt")  # Có thể đổi thành "yolov8m.pt" để có độ chính xác cao hơn

# Đọc ảnh
image_path = "C:\\Users\\TV\\Documents\\BTTH_Python\\test\\hinh-anh-5-1483195275227.jpg"  # Thay bằng ảnh của bạn
image = cv2.imread(image_path)

# Dự đoán đối tượng trong ảnh
results = model(image)

# Danh sách nhãn của YOLOv8
object_names = model.names

# Phân loại đối tượng vào nhóm: người, động vật, thực vật
humans = []
animals = []
plants = []  # YOLO mặc định ít hỗ trợ thực vật, cần mô hình chuyên dụng để nhận diện tốt hơn

# Các ID lớp (class) đại diện cho con người, động vật, thực vật
human_class = [0]  # 0 là 'person' theo YOLOv8
animal_classes = [15, 16, 17, 18, 19, 20, 21]  # Dog, horse, bird, cow, sheep, elephant, bear,...
plant_classes = []  # YOLOv8 không hỗ trợ trực tiếp, cần mô hình khác hoặc tự gán nhóm

# Duyệt qua từng kết quả để phân loại đối tượng
for result in results:
    boxes = result.boxes.xyxy.cpu().numpy()  # Lấy tọa độ hộp
    class_ids = result.boxes.cls.cpu().numpy()  # Lấy ID của các lớp đối tượng

    for box, class_id in zip(boxes, class_ids):
        x1, y1, x2, y2 = map(int, box)
        label = object_names[int(class_id)]  # Lấy tên đối tượng

        # Xác định nhóm đối tượng
        if int(class_id) in human_class:
            humans.append(label)
            color = (0, 0, 255)  # Màu đỏ cho con người
        elif int(class_id) in animal_classes:
            animals.append(label)
            color = (255, 0, 0)  # Màu xanh cho động vật
        elif int(class_id) in plant_classes:
            plants.append(label)
            color = (0, 255, 0)  # Màu xanh lá cho thực vật
        else:
            color = (200, 200, 200)  # Màu xám cho đối tượng khác

        # Vẽ bounding box và tên đối tượng
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Đếm số lượng từng loại đối tượng
num_humans = len(humans)
num_animals = len(animals)
num_plants = len(plants)

# In kết quả
print(f"Số lượng con người: {num_humans}")
print(f"Số lượng động vật: {num_animals}")
print(f"Số lượng thực vật: {num_plants}")

# Hiển thị ảnh kết quả
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
