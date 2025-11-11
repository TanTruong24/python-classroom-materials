# 09_write_multiple_lines.py
# Mục tiêu: 2 cách phổ biến để ghi nhiều dòng text

lines = ["Dòng thứ nhất", "Dòng thứ hai", "Dòng thứ ba"]

# Cách 1: writelines() cần tự thêm "\n"
with open("file1.txt", "w", encoding="utf-8") as f:
    f.writelines(line + "\n" for line in lines)
print("Đã ghi file1.txt bằng writelines().")

# Cách 2: join chuỗi rồi write một lần
text = "\n".join(lines) + "\n"  # thêm \n cuối nếu muốn
with open("file2.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Đã ghi file2.txt bằng '\\n'.join() + write().")
