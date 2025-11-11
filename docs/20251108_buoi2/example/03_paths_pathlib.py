# 03_paths_pathlib.py

from pathlib import Path

# Thư mục hiện tại của file đang chạy
base = Path(__file__).parent

print("Thư mục hiện tại:", base)

# File trong cùng thư mục
file1 = base / "input.txt"

# File trong thư mục con data/
file2 = base / "data" / "input.txt"

# File nằm ngoài thư mục hiện tại (parent)
file3 = base.parent / "config.json"

def safe_read(path: Path, label: str):
    print(f"\nĐọc {label}: {path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Không tìm thấy file: {path}")

safe_read(file1, "file1 (cùng thư mục)")
safe_read(file2, "file2 (trong thư mục con data)")
safe_read(file3, "file3 (ở thư mục cha)")
