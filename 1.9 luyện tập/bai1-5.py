
# BÀI 1: Tính tổng list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tong = sum(list1)
print("Bài 1 - Tổng:", tong)



# BÀI 2: Tính tích list

list2 = [1, 2, 3, 4, 5]

tich = 1
for i in list2:
    tich *= i

print("Bài 2 - Tích:", tich)


# BÀI 3: Tách chẵn lẻ
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_list = []
odd_list = []

for i in list3:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Bài 3 - Số chẵn:", even_list)
print("Bài 3 - Số lẻ:", odd_list)



# BÀI 4: Lấy phần tử vị trí 2 và 3

list4 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

new_list4 = list4[2:4]  # lấy vị trí 2 và 3
print("Bài 4:", new_list4)



# BÀI 5: Thêm phần tử vào list

list5 = ['zero', 'three']

# chèn 'one' và 'two' vào giữa
list5.insert(1, 'one')
list5.insert(2, 'two')

print("Bài 5:", list5)