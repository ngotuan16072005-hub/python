
# BÀI 11

# List cho trước
list11 = ['3', '4', '5', '6', '7', '8']

# Nhập n từ bàn phím
n = int(input("Nhập n: "))

# Tìm các từ có độ dài > n
result11 = []
for word in list11:
    if len(word) > n:
        result11.append(word)

print("Bài 11 - Các từ có độ dài > n:", result11)


# BÀI 12

list12 = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

# Nhập độ dài
k = int(input("Nhập độ dài k: "))

count = 0
for s in list12:
    if len(s) >= k and s[0] == s[-1]:
        count += 1

print("Bài 12 - Số chuỗi thỏa mãn:", count)