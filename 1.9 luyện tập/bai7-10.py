
# BÀI 7

list7 = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

# Cách 1: Loại bỏ hoàn toàn phần tử trùng (chỉ giữ phần tử xuất hiện 1 lần)
new1 = []
for i in list7:
    if list7.count(i) == 1:
        new1.append(i)

print("Bài 7 - Loại bỏ phần tử trùng hoàn toàn:", new1)

# Cách 2: Giữ lại 1 phần tử nếu bị trùng
new2 = []
for i in list7:
    if i not in new2:
        new2.append(i)

print("Bài 7 - Giữ 1 phần tử:", new2)



# BÀI 8: Số lớn nhất

list8 = [11, 2, 23, 45, 6, 9]

max_value = max(list8)
print("Bài 8 - Số lớn nhất:", max_value)



# BÀI 9: Số nhỏ nhất

list9 = [11, 2, 23, 45, 6, 9]

min_value = min(list9)
print("Bài 9 - Số nhỏ nhất:", min_value)



# BÀI 10: Copy list

list10 = [1, 2, 3, 4, 5]

# Cách 1
copy_list1 = list10.copy()

# Cách 2
copy_list2 = list10[:]

print("Bài 10 - :", copy_list1)
print("Bài 10 - :", copy_list2)