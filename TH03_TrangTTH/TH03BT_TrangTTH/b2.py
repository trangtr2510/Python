# Bài 15_b: Viết hàm cho các bài đã thực hiện 
# 4) Viết hàm bmi_show(): Trả về nhận xét dựa vào chỉ số BMI đã tính với 2 tham số truyền vào là chiều 
# cao, cân nặng (Xem lại bài tập số 7) 
# 5) Viết hàm cal_point(): Trả về điểm trung bình hệ 10 và hệ 4 của một học sinh khi truyền vào danh sách 
# điểm (Xem lại bài tập số 10 ý 2) 
# 6) Viết hàm list_prime(): trả danh sách các số nguyên tố trong khoảng tử 1 đến n với tham số truyền 
# vào là n (Xem lại bài tập số 12) 

# Hàm tính và trả về nhận xét dựa trên chỉ số BMI
def bmi_show(height: float, weight: float) -> str:
    try:
        if height <= 0 or weight <= 0:
            return "Chiều cao và cân nặng phải lớn hơn 0."
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            return f"Chỉ số BMI của bạn là: {bmi}. Bạn đang thiếu cân (Underweight)."
        elif 18.5 <= bmi <= 24.9:
            return f"Chỉ số BMI của bạn là: {bmi}. Bạn có cân nặng bình thường (Normal weight)."
        elif 25 <= bmi <= 29.9:
            return f"Chỉ số BMI của bạn là: {bmi}. Bạn thừa cân (Overweight)."
        else:
            return f"Chỉ số BMI của bạn là: {bmi}. Bạn béo phì (Obese)."
    except ValueError:
        return "Vui lòng nhập đầu vào hợp lệ."

# Hàm tính điểm trung bình hệ 10 và hệ 4
def cal_point(scores: list[float]) -> tuple[float, float]:
    if not scores:
        return 0.0, 0.0
    average_10 = sum(scores) / len(scores)
    average_4 = average_10 / 10 * 4
    return round(average_10, 2), round(average_4, 2)

# Hàm kiểm tra số nguyên tố
def list_prime(n: int) -> list[int]:
    primes = []
    if n < 2:
        return primes
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

# Menu cho chương trình chính
def main():
    while True:
        print("\nChọn hành động:")
        print("1. Hiển thị nhận xét BMI")
        print("2. Tính điểm trung bình hệ 10 và hệ 4")
        print("3. Hiển thị danh sách số nguyên tố trong khoảng từ 1 đến N")
        print("4. Thoát")

        try:
            choice = int(input("Nhập lựa chọn của bạn (1/2/3/4): "))

            if choice == 1:
                # Lựa chọn 1: Hiển thị nhận xét BMI
                height = float(input("Nhập chiều cao (m): "))
                weight = float(input("Nhập cân nặng (kg): "))
                print(bmi_show(height, weight))

            elif choice == 2:
                # Lựa chọn 2: Tính điểm trung bình
                n = int(input("Nhập số lượng điểm: "))
                scores = []
                print("Nhập các điểm hệ 10:")
                for i in range(n):
                    while True:
                        try:
                            score = float(input(f"Nhập điểm thứ {i + 1}: "))
                            if 0 <= score <= 10:
                                scores.append(score)
                                break
                            else:
                                print("Vui lòng nhập điểm trong khoảng từ 0 đến 10.")
                        except ValueError:
                            print("Vui lòng nhập số hợp lệ.")
                letter_grades = []
                for score in scores:
                    if score >= 9:
                        letter_grades.append("A+")
                    elif score >= 8.5:
                        letter_grades.append("A")
                    elif score >= 8:
                        letter_grades.append("B+")
                    elif score >= 7:
                        letter_grades.append("B")
                    elif score >= 6.5:
                        letter_grades.append("C+")
                    elif score >= 5.5:
                        letter_grades.append("C")
                    elif score >= 5:
                        letter_grades.append("D+")
                    elif score >= 4:
                        letter_grades.append("D")
                    else:
                        letter_grades.append("F")

                average_10, average_4 = cal_point(scores)

                print("Điểm hệ 10:", scores)
                print("Điểm chữ tương ứng:", letter_grades)
                print("Điểm trung bình hệ 10:", average_10)
                print("Điểm trung bình hệ 4:", average_4)

            elif choice == 3:
                # Lựa chọn 3: Hiển thị số nguyên tố trong khoảng từ 1 đến N
                n = int(input("Nhập số N: "))
                if n >= 2:
                    primes = list_prime(n)
                    print(f"Dãy số nguyên tố từ 2 đến {n}: {primes}")
                else:
                    print("Vui lòng nhập số N lớn hơn hoặc bằng 2.")

            elif choice == 4:
                # Lựa chọn 4: Thoát chương trình
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break

            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ.")

# Chạy chương trình
if __name__ == "__main__":
    main()
