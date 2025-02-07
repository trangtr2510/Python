import pandas as pd

# Đọc toàn bộ các sheet từ file Excel
file_name = "excel_Data_Movies.xlsx"
sheets = pd.read_excel(file_name, sheet_name=None)  # None để đọc tất cả sheet

# Lặp qua từng sheet và hiển thị dữ liệu
for sheet_name, df in sheets.items():
    print(f"Sheet: {sheet_name}")
    print(df.head())  # Hiển thị 5 dòng đầu của mỗi sheet
    print("-" * 50)


