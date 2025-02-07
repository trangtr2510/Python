import pandas as pd

# Đường dẫn tới file Excel
path_excel = "Data_Excel.xlsx"  

# Đọc dữ liệu từ file Excel
data_ex41 = pd.read_excel(
    path_excel, 
    sheet_name='4080130_03',  # Chọn sheet cần đọc
    header=None,              # Không có dòng tiêu đề
    usecols=[1, 6, 7, 8, 9, 10],  # Chỉ lấy các cột mong muốn
    index_col=0                # Đặt cột đầu tiên làm index
)

# Hiển thị thông tin của DataFrame
print("Thông tin của DataFrame:")
print(data_ex41.info())

# Hiển thị 5 dòng dữ liệu đầu tiên
print("\n5 dòng dữ liệu đầu tiên:")
print(data_ex41.head())
