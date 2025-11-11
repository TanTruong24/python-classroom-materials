# 05_read_methods.py
# Mục tiêu: phân biệt 3 cách đọc file: read, readline, readlines

filename = "input.txt"

# read(): đọc toàn bộ file thành 1 chuỗi
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
    print("== read() ==")
    print(repr(content))   # dùng repr để thấy cả ký tự xuống dòng \n

# readline(): đọc từng dòng một mỗi lần gọi
with open(filename, "r", encoding="utf-8") as f:
    print("\n== readline() nhiều lần ==")
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    print("line1:", repr(line1))
    print("line2:", repr(line2))
    print("line3:", repr(line3))

# readlines(): đọc toàn bộ file thành list các dòng
with open(filename, "r", encoding="utf-8") as f:
    print("\n== readlines() ==")
    lines = f.readlines()
    print(lines)
