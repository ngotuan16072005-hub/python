# 1. Tổng 2 số
def tong_2_so(a, b):
    return a + b

# 2. Tổng nhiều số
def tong_n_so(*args):
    return sum(args)

# 3. Kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. Tìm số nguyên tố trong khoảng
def tim_snt(a, b):
    return [i for i in range(a, b + 1) if la_so_nguyen_to(i)]

# 5. Kiểm tra số hoàn hảo
def la_so_hoan_hao(n):
    if n <= 0:
        return False
    tong = sum(i for i in range(1, n) if n % i == 0)
    return tong == n

# 6. Tìm số hoàn hảo trong khoảng
def tim_so_hoan_hao(a, b):
    return [i for i in range(a, b + 1) if la_so_hoan_hao(i)]

# 7. Menu
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Tổng 2 số")
        print("2. Tổng nhiều số")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm số nguyên tố trong khoảng")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm số hoàn hảo trong khoảng")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Kết quả:", tong_2_so(a, b))

        elif choice == "2":
            ds = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))
            print("Kết quả:", tong_n_so(*ds))

        elif choice == "3":
            n = int(input("Nhập n: "))
            print("Là SNT" if la_so_nguyen_to(n) else "Không phải SNT")

        elif choice == "4":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Các SNT:", tim_snt(a, b))

        elif choice == "5":
            n = int(input("Nhập n: "))
            print("Là số hoàn hảo" if la_so_hoan_hao(n) else "Không phải")

        elif choice == "6":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Các số hoàn hảo:", tim_so_hoan_hao(a, b))

        elif choice == "0":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")

# Chạy chương trình
menu()