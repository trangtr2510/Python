import pandas as pd

# Đọc file CSV
df = pd.read_csv('csv_Data_Loan.csv')

# Tách thành 2 DataFrame dựa trên kiểu dữ liệu
# DataFrame chứa các cột số
df_number = df.select_dtypes(include=['int64', 'float64'])

# DataFrame chứa các cột object
df_object = df.select_dtypes(include=['object'])

# Hiển thị 5 dòng đầu tiên của df_number
print("5 dòng đầu tiên của df_number:")
print(df_number.head())

print("\n5 dòng đầu tiên của df_object:")
print(df_object.head())

# Hiển thị thông tin về các cột trong mỗi DataFrame
print("\nCác cột trong df_number:")
print(df_number.columns.tolist())

print("\nCác cột trong df_object:")
print(df_object.columns.tolist())