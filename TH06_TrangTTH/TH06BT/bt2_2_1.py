import pandas as pd

# Đọc file CSV với các tham số mặc định
df = pd.read_csv('csv_Data_Loan.csv')

# Hiển thị 5 dòng đầu tiên của dữ liệu
print("5 dòng đầu tiên của dữ liệu:")
print(df.head())

# Hiển thị thông tin cơ bản về dataset
print("\nThông tin cơ bản về dataset:")
print(df.info())

# Hiển thị thống kê mô tả của dữ liệu số
print("\nThống kê mô tả của dữ liệu số:")
print(df.describe())