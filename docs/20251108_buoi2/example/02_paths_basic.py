# 02_paths_basic.py

# Ví dụ minh họa các kiểu đường dẫn (chạy trên Windows chỉ là ví dụ, tùy chỉnh theo máy)

# 1. Đường dẫn tuyệt đối
# Lỗi nếu không file không đúng đường dẫn
abs_path = r"C:\Users\Minh\Desktop\data.txt"
print("Đọc bằng đường dẫn tuyệt đối:")
with open(abs_path, "r", encoding="utf-8") as f:
    print(f.read())

# 2. Đường dẫn tương đối - file cùng thư mục với script
#   Giả sử file input.txt nằm cùng thư mục
rel_same = "input.txt"
print("\nĐọc file cùng thư mục (đường dẫn tương đối):")
with open(rel_same, "r", encoding="utf-8") as f:
    print(f.read())

# 3. Đường dẫn tương đối - file trong thư mục con
#   Ví dụ: data/input.txt
# sử dụng try: except để bắt lỗi, không bị dừng chương trình
rel_sub = "data/input.txt"
print("\nĐọc file trong thư mục con data/:")
try:
    with open(rel_sub, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"Không tìm thấy file: {rel_sub}")

# 4. Đường dẫn tương đối - lùi 1 cấp thư mục
#   Nếu script nằm trong output/main.py, dùng: ../data/input.txt
