import requests
import pandas as pd

# Địa chỉ API với từ khóa "VIRUS" trong tiêu đề
url = "http://api.plos.org/search?q=title:VIRUS&fl=id,eissn,author_display,abstract,title_display,score"

# Gửi yêu cầu GET
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công
if response.status_code == 200:
    data = response.json()
    
    # Trích xuất danh sách bài báo
    docs = data.get("response", {}).get("docs", [])

    # Tạo DataFrame từ dữ liệu
    df = pd.DataFrame(docs, columns=["id", "eissn", "author_display", "abstract", "title_display", "score"])
    
    # Lưu vào tệp CSV
    df.to_csv("Paper.csv", index=False, encoding="utf-8")
    
    print("Dữ liệu đã được lưu vào Paper.csv")
else:
    print("Lỗi khi lấy dữ liệu từ API:", response.status_code)
