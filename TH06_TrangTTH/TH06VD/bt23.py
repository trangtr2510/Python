import pandas as pd

# Đường dẫn đến tệp Excel
path_excel = "Data_Excel.xlsx"  

# Đọc dữ liệu từ sheet đầu tiên, chỉ lấy các cột cần thiết
data_ex1 = pd.read_excel(path_excel,
                         sheet_name=0,       # Đọc từ sheet đầu tiên
                         usecols=[1, 6, 7, 8, 9, 10],  # Lấy các cột chỉ định
                         index_col=0)        # Đặt cột đầu tiên làm index (Mã SV)

# Hiển thị thông tin về DataFrame
print("Thông tin về DataFrame:")
print(data_ex1.info())

# Hiển thị 5 dòng dữ liệu đầu tiên
print("\n5 dòng dữ liệu đầu tiên:")
print(data_ex1.head())
