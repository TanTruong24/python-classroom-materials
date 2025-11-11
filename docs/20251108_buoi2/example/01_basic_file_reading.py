# 01_basic_file_reading.py

# Cách cơ bản: open → read → close
file = open("input.txt", "r", encoding="utf-8")

# Đọc toàn bộ nội dung
content = file.read()
print("Nội dung file (cách 1):")
print(content)

# Đóng file
file.close()

# Khuyến nghị: dùng with để không quên close()
print("\nNội dung file (cách 2 - with):")
with open("input.txt", "r", encoding="utf-8") as f:
    content2 = f.read()
    print(content2)
