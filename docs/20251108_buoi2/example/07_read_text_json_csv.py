# 07_read_text_json_csv.py
# Mục tiêu: cách đọc 3 loại file phổ biến: txt, json, csv

import json
import csv

# 1. TXT: đọc đơn giản như chuỗi
with open("input.txt", "r", encoding="utf-8") as f:
    print("== TXT ==")
    print(f.read())

# 2. JSON: dùng json.load() để parse thành dict/list Python
with open("data.json", "r", encoding="utf-8") as f:
    print("\n== JSON ==")
    data = json.load(f)
    print("Kiểu dữ liệu:", type(data))
    print("Nội dung:", data)

# 3. CSV: mỗi dòng là list các cột
with open("data.csv", newline="", encoding="utf-8") as f:
    print("\n== CSV ==")
    reader = csv.reader(f)
    for row in reader:
        # row là list, ví dụ: ["Minh", "25"]
        print("Dòng:", row)
