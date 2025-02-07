import pandas as pd

# Đường dẫn tới tệp Excel (thay bằng đường dẫn thực tế)
path_excel = "Data_Excel.xlsx"  

# Đọc dữ liệu từ sheet '4080130_03' (không có dòng tiêu đề)
data_ex4 = pd.read_excel(path_excel, sheet_name='4080130_03', header=None)

# Hiển thị thông tin của DataFrame
print("Thông tin của DataFrame:")
print(data_ex4.info())

# Hiển thị 5 dòng dữ liệu đầu tiên
print("\n5 dòng dữ liệu đầu tiên:")
print(data_ex4.head())
