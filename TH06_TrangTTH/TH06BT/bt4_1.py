from pymongo import MongoClient
import pandas as pd

# Kết nối tới MongoDB
client = MongoClient("mongodb://localhost:27017/")  # URI đúng cho MongoDB
db = client["your_database_name"]  # Tên database
collection = db["LC_Meteorology"]  # Tên collection

# Truy vấn dữ liệu
query = {"Id": "LC"}
fields = {"_id": 0, "Time": 1, "Rain": 1, "T2m": 1}
cursor = collection.find(query, fields).sort("Time", -1).limit(1000)

# Kiểm tra có dữ liệu không
if len(list(cursor)) > 0:
    # Quay lại con trỏ nếu đã duyệt qua hết
    cursor.rewind()

    # Chuyển đổi dữ liệu sang DataFrame
    df_lc = pd.DataFrame(list(cursor))
    
    # Hiển thị thông tin DataFrame
    print(df_lc.info())
    print(df_lc.head(10))  # Hiển thị 10 dòng đầu tiên
else:
    print("Không có dữ liệu phù hợp với truy vấn.")
    

#4.2
import pymongo
import pandas as pd

# Kết nối đến MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Thay đổi nếu cần
db = client["your_database_name"]  # Thay đổi tên database của bạn
collection = db["LC_Stations"]

# Đọc toàn bộ dữ liệu từ Collection LC_Stations
data = list(collection.find({}, {"_id": 0}))  # Loại bỏ _id nếu không cần

# Chuyển dữ liệu thành DataFrame
df_station = pd.DataFrame(data)

# Hiển thị DataFrame
print(df_station)

#5.1
from sklearn.datasets import load_wine
import pandas as pd

# Tải dữ liệu Wine dataset
wine = load_wine()

# Đọc dữ liệu dưới dạng ndarray
X_ndarray = wine.data  # Biến đầu vào (features)
y_ndarray = wine.target  # Nhãn của các mẫu

# Chuyển đổi dữ liệu sang DataFrame
df_wine = pd.DataFrame(X_ndarray, columns=wine.feature_names)
df_wine["class"] = y_ndarray  # Thêm cột class

# Hiển thị một số mẫu rượu trong tập dữ liệu
print("Dữ liệu dưới dạng ndarray:")
print(X_ndarray[:5])  # Hiển thị 5 mẫu đầu tiên
print("\nDữ liệu dưới dạng DataFrame:")
print(df_wine.head())  # Hiển thị 5 dòng đầu tiên

#5.2
from sklearn.datasets import (
    fetch_olivetti_faces,
    fetch_20newsgroups,
    fetch_20newsgroups_vectorized,
    fetch_lfw_people,
    fetch_lfw_pairs,
    fetch_covtype,
    fetch_rcv1,
    fetch_kddcup99,
    fetch_california_housing
)
import numpy as np

def explore_dataset(dataset, name):
    """Hàm hiển thị thông tin cơ bản về dataset"""
    print(f"\n=== {name} ===")
    print(f"Kích thước dữ liệu: {dataset.data.shape}")
    if hasattr(dataset, 'target'):
        print(f"Kích thước nhãn: {dataset.target.shape}")
    if hasattr(dataset, 'target_names'):
        print(f"Các nhãn: {dataset.target_names}")
    print(f"Keys có sẵn trong dataset: {dataset.keys()}")
    print("-" * 50)

# 1. Olivetti faces dataset
faces = fetch_olivetti_faces()
explore_dataset(faces, "Olivetti Faces Dataset")

# 2. 20 Newsgroups dataset
newsgroups = fetch_20newsgroups()
explore_dataset(newsgroups, "20 Newsgroups Dataset")

# 3. 20 Newsgroups Vectorized
news_vectorized = fetch_20newsgroups_vectorized()
explore_dataset(news_vectorized, "20 Newsgroups Vectorized Dataset")

# 4. LFW People dataset
lfw_people = fetch_lfw_people(min_faces_per_person=70)
explore_dataset(lfw_people, "LFW People Dataset")

# 5. LFW Pairs dataset
lfw_pairs = fetch_lfw_pairs()
explore_dataset(lfw_pairs, "LFW Pairs Dataset")

# 6. Covertype dataset
covtype = fetch_covtype(data_home='data', random_state=42)
explore_dataset(covtype, "Covertype Dataset")

# 7. RCV1 dataset
rcv1 = fetch_rcv1(random_state=42)
explore_dataset(rcv1, "RCV1 Dataset")

# 8. KDD Cup 99 dataset
kddcup = fetch_kddcup99(random_state=42)
explore_dataset(kddcup, "KDD Cup 99 Dataset")

# 9. California Housing dataset
housing = fetch_california_housing()
explore_dataset(housing, "California Housing Dataset")

#6.1 
# Phần 1: Bài toán phân lớp với Decision Tree
import numpy as np
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

# Tạo dataset cho bài toán phân lớp
print("=== Bài toán phân lớp ===")
X_clf, y_clf = make_classification(
    n_samples=1000,      # 1000 mẫu
    n_features=8,        # 8 đặc trưng
    n_classes=2,         # 2 lớp
    random_state=42      # Để kết quả có thể tái tạo lại được
)

# Tạo và huấn luyện mô hình Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_clf, y_clf)

# In kết quả
print(f"Kích thước dữ liệu: {X_clf.shape}")
print(f"Số lượng mẫu cho mỗi lớp: {np.bincount(y_clf)}")
print(f"Độ chính xác của mô hình: {dt_model.score(X_clf, y_clf):.4f}")

# Phần 2: Bài toán phân cụm và trực quan hóa
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def create_cluster_dataset(cluster_std):
    # Tạo dataset
    X, y = make_blobs(
        n_samples=10000,     # 10000 mẫu
        n_features=2,        # 2 đặc trưng
        centers=5,           # 5 tâm cụm
        cluster_std=cluster_std,  # Độ phân tán của cụm
        random_state=42
    )
    
    # Vẽ biểu đồ scatter
    plt.figure(figsize=(10, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    plt.colorbar()
    plt.title(f'Biểu đồ phân cụm (cluster_std={cluster_std})')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
    
    return X, y

print("\n=== Bài toán phân cụm ===")
# Tạo dataset với cluster_std = 0.5
X_cluster, y_cluster = create_cluster_dataset(0.5)
print(f"Kích thước dữ liệu phân cụm: {X_cluster.shape}")
print(f"Số lượng cụm: {len(np.unique(y_cluster))}")

# Thử nghiệm với các giá trị cluster_std khác nhau
print("\nThử nghiệm với các giá trị cluster_std khác nhau:")
std_values = [0.1, 0.3, 0.7, 1.0]
for std in std_values:
    print(f"\nTạo dataset với cluster_std = {std}")
    X, y = create_cluster_dataset(std)

print("\nNhận xét về ảnh hưởng của tham số cluster_std:")
print("1. cluster_std = 0.1: Các cụm rất tập trung, ranh giới rõ ràng")
print("2. cluster_std = 0.3: Các cụm vẫn tách biệt nhưng bắt đầu có sự phân tán")
print("3. cluster_std = 0.5: Các cụm phân tán vừa phải, vẫn có thể phân biệt được")
print("4. cluster_std = 0.7: Các cụm bắt đầu có sự chồng lấn")
print("5. cluster_std = 1.0: Các cụm chồng lấn nhiều, khó phân biệt ranh giới")
