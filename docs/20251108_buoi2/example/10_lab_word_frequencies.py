# 10_lab_word_frequencies.py
# Mục tiêu:
# - Đọc tên file từ input()
# - File CSV 1 dòng chứa các từ, phân tách bởi dấu phẩy
# - Đếm số lần xuất hiện của từng từ và in ra

import csv

filename = input().strip()
freq = {}

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        # row là list các từ, ví dụ: ["apple", "orange", "apple"]
        for word in row:
            w = word.strip()
            if not w:      # bỏ qua chuỗi rỗng
                continue
            freq[w] = freq.get(w, 0) + 1

for w, c in freq.items():
    print(f"{w} - {c}")
