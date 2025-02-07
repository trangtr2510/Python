import pandas as pd

# Đường dẫn đến tệp Excel 
path_excel = "Data_Excel.xlsx" 

# Đọc dữ liệu từ sheet 2, bắt đầu từ dòng 9
data_ex3 = pd.read_excel(path_excel,
                         sheet_name='4080130_02',  # Chỉ định sheet cần đọc
                         skiprows=9)  # Bỏ qua 8 dòng đầu tiên, đọc từ dòng 9

# Hiển thị thông tin của DataFrame
data_ex3.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex3.head()
