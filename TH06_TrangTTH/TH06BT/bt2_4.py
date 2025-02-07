import pandas as pd

# Đọc dữ liệu từ file JSON
file_name = "json_Data_flights.json"
data_json = pd.read_json(file_name)

# Hiển thị 5 dòng đầu tiên
print(data_json.head())
