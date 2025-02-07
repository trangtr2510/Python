import pandas as pd

# Đường dẫn đến file Excel
path_excel = 'Data_Excel.xlsx'

# Đọc dữ liệu từ file Excel
# Mặc định sẽ đọc sheet đầu tiên (4080130_01)
data_ex = pd.read_excel(path_excel)

# Hiển thị thông tin về DataFrame
print("Thông tin về DataFrame:")
print(data_ex.info())

# Hiển thị 5 dòng đầu tiên của dữ liệu
print("\n5 dòng đầu tiên của dữ liệu:")
print(data_ex.head())

# Nếu muốn đọc một sheet cụ thể, có thể chỉ định tham số sheet_name
# Ví dụ đọc sheet thứ 2:
data_ex_sheet2 = pd.read_excel(path_excel, sheet_name='4080130_02')
print("\n5 dòng đầu tiên của sheet 4080130_02:")
print(data_ex_sheet2.head())

