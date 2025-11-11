# 06_read_line_by_line.py
# Mục tiêu: cách đọc file từng dòng mà không cần load hết vào bộ nhớ

filename = "input.txt"

print("== for line in file ==")
with open(filename, "r", encoding="utf-8") as f:
    # File object là một iterator, có thể duyệt trực tiếp
    for line in f:
        print(line.strip())  # strip() bỏ \n và khoảng trắng 2 đầu

print("\n== while + readline() ==")
with open(filename, "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:  # khi line == "" tức là hết file
            break
        print(line.strip())
