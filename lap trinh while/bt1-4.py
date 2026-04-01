while True:
    print("\n===== MENU =====")
    print("1. Tính tích 10 số tự nhiên đầu tiên")
    print("2. Tính giai thừa n (n!)")
    print("3. Kiểm tra số nguyên tố")
    print("4. Tổng các số chẵn nhỏ hơn n")
    print("0. Thoát")

    chon = input("Nhập lựa chọn: ")

    # --- Bài 1 ---
    if chon == "1":
        tich = 1
        i = 1
        while i <= 10:
            tich *= i
            i += 1
        print("Kết quả:", tich)

    # --- Bài 2 ---
    elif chon == "2":
        n = int(input("Nhập n: "))
        giai_thua = 1
        i = 1
        while i <= n:
            giai_thua *= i
            i += 1
        print(f"Giai thừa của {n} là:", giai_thua)

    # --- Bài 3 ---
    elif chon == "3":
        n = int(input("Nhập n: "))
        if n < 2:
            print("Không phải số nguyên tố")
        else:
            i = 2
            la_snt = True
            while i <= n // 2:
                if n % i == 0:
                    la_snt = False
                    break
                i += 1

            if la_snt:
                print("Đây là số nguyên tố")
            else:
                print("Không phải số nguyên tố")

    # --- Bài 4 ---
    elif chon == "4":
        n = int(input("Nhập n: "))
        tong = 0
        i = 1
        while i < n:
            if i % 2 == 0:
                tong += i
            i += 1
        print("Tổng là:", tong)

    # --- Thoát ---
    elif chon == "0":
        print("Thoát chương trình thành công!")
        break

    else:
        print("Lựa chọn không hợp lệ!")