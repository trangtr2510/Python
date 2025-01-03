# Xác định nguyên âm|Phụ âm
print("Bai 6")
n = input("Nhập 1 chữ cái: ").lower()
if n in 'aeiou':
    print(f"{n} là nguyên âm")
elif n.isalpha():
    print(f"{n} là phụ âm")
else:
    print(f"{n} không phải chữ cái")
