#Xác định mùa trong năm
# Nhập vào tháng sinh
thang_sinh = int(input("Nhập vào tháng sinh của bạn (1-12): "))

# Kiểm tra và xác định mùa
if thang_sinh <= 3:
    print("Bạn sinh vào Mùa xuân.")
elif thang_sinh <= 6:
    print("Bạn sinh vào Mùa hạ.")
elif thang_sinh <= 9:
    print("Bạn sinh vào Mùa thu.")
elif thang_sinh <= 12:
    print("Bạn sinh vào Mùa đông.")
else:
    print("Tháng sinh nhập vào không đúng.")
