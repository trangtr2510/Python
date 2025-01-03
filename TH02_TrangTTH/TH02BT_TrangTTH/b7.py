#Tính chỉ số BMI 
print("Bai 7")
weight = float(input("Nhập cân nặng(kg): "))
height = float(input("Nhập chiều cao(m): "))

bmi = weight / (height ** 2)
print("Chỉ số bmi của bạn là: {bmi}")

if bmi < 18.5:
    print("Bạn đang thiếu cân (Underweight).")
elif 18.5 <= bmi <= 24.9:
    print("Bạn có cân nặng bình thường (Normal weight).")
elif 25 <= bmi <= 29.9:
    print("Bạn thừa cân (Overweight).")
else:
    print("Bạn béo phì (Obese).")