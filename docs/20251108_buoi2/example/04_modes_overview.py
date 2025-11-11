# 04_modes_overview.py

# File này sẽ tạo / ghi đè một số file demo

# 1. "w" - ghi mới: tạo file nếu chưa có, xóa nội dung cũ nếu đã tồn tại
with open("demo_w.txt", "w", encoding="utf-8") as f:
    f.write("Ghi bằng mode 'w' - ghi mới / ghi đè.\n")

print("Đã ghi demo_w.txt bằng mode 'w'.")

# 2. "a" - append: ghi nối vào cuối file, tạo mới nếu chưa có
with open("demo_a.txt", "a", encoding="utf-8") as f:
    f.write("Dòng mới được thêm bằng mode 'a'.\n")

print("Đã ghi demo_a.txt bằng mode 'a'.")

# 3. "x" - create: chỉ tạo file mới, lỗi nếu đã tồn tại
try:
    with open("demo_x.txt", "x", encoding="utf-8") as f:
        f.write("File này được tạo bằng mode 'x'.\n")
    print("Đã tạo demo_x.txt bằng mode 'x'.")
except FileExistsError:
    print("demo_x.txt đã tồn tại, không thể tạo lại bằng mode 'x'.")

# 4. "r" - read: chỉ đọc, lỗi nếu file không tồn tại
try:
    with open("demo_w.txt", "r", encoding="utf-8") as f:
        print("\nNội dung demo_w.txt:")
        print(f.read())
except FileNotFoundError:
    print("demo_w.txt không tồn tại.")

# 5. "r+" - đọc & ghi, bắt buộc file phải tồn tại
try:
    with open("demo_r_plus.txt", "r+", encoding="utf-8") as f:
        # ví dụ: đọc rồi ghi đè từ đầu
        old = f.read()
        print("\nNội dung cũ demo_r_plus.txt:", old)
        f.seek(0)
        f.write("Nội dung mới bằng r+")
except FileNotFoundError:
    print("\ndemo_r_plus.txt chưa tồn tại, hãy tạo trước khi dùng 'r+'.")

# 6. "w+" - đọc & ghi, nhưng luôn ghi mới từ đầu, tạo file nếu chưa có
with open("demo_w_plus.txt", "w+", encoding="utf-8") as f:
    f.write("Ghi bằng w+.\n")
    f.seek(0)
    print("\nNội dung demo_w_plus.txt (đọc lại):")
    print(f.read())

"""
hàm seek() liên quan tới vị trí con trỏ trong file
- Mỗi file khi mở ra sẽ có một con trỏ đọc/ghi (file pointer) cho biết đang đứng ở vị trí thứ mấy trong file.
- Hàm seek() dùng để di chuyển con trỏ tới vị trí mình muốn.
Cú pháp cơ bản:

cú pháp: f.seek(offset, whence)
- offset: số byte muốn nhảy tới.
- whence: mốc tính (thường là):
    + 0: tính từ đầu file (mặc định, nên nhiều khi người ta chỉ viết f.seek(0)).
    + 1: tính từ vị trí hiện tại.
    + 2: tính từ cuối file.
"""