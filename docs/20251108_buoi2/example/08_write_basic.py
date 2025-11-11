# 08_write_basic.py
# Mục tiêu: ghi dữ liệu ra 3 định dạng: txt, csv, json

import csv
import json

# 1. Ghi file TXT
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Dòng 1\n")
    f.write("Dòng 2\n")
print("Đã ghi output.txt")

# 2. Ghi file CSV
rows = [
    ["Name", "Age"],
    ["Minh", 25],
    ["Anna", 30],
]

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("Đã ghi data.csv")

# 3. Ghi file JSON
info = {
    "name": "Minh",
    "age": 25,
    "skills": ["Python", "React"],
}

with open("data.json", "w", encoding="utf-8") as f:
    # ensure_ascii=False để giữ tiếng Việt, indent để dễ đọc
    json.dump(info, f, ensure_ascii=False, indent=4)
print("Đã ghi data.json")
