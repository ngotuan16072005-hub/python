def bai1():
    n = int(input("Nhập số dòng cần đọc: "))
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            for i in range(n):
                line = f.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print("Không tìm thấy file input.txt")


def bai2():
    text = input("Nhập đoạn văn: ")
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("Đã ghi vào file. Nội dung file là:")
    with open("output.txt", "r", encoding="utf-8") as f:
        print(f.read())


def bai3():
    # Tạo file
    with open("demo_file1.txt", "w", encoding="utf-8") as f:
        f.write("Thuc\nhanh\nvoi\nfile\nIO\n")

    print("\na) Nội dung trên 1 dòng:")
    with open("demo_file1.txt", "r", encoding="utf-8") as f:
        content = f.read().replace("\n", " ")
        print(content)

    print("\nb) Nội dung theo từng dòng:")
    with open("demo_file1.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())


def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Đọc n dòng đầu file")
        print("2. Ghi và đọc file")
        print("3. Tạo và xử lý demo_file1.txt")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            bai1()
        elif choice == "2":
            bai2()
        elif choice == "3":
            bai3()
        elif choice == "0":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


# Chạy chương trình
menu()