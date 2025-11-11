# Đọc tên file đầu vào
filename = input().strip()

# Đọc toàn bộ nội dung file
with open(filename, 'r') as file:
    lines = file.readlines()

# Tạo dictionary: key = số mùa, value = list tên phim
shows = {}

# Duyệt từng cặp dòng (số mùa, tên phim)
for i in range(0, len(lines), 2):
    num = int(lines[i].strip())       # số mùa
    title = lines[i + 1].strip()      # tên phim

    if num not in shows:
        shows[num] = []
    shows[num].append(title)

# --- Ghi file output_keys.txt ---
with open("output_keys.txt", "w") as f:
    for key in sorted(shows.keys(), reverse=True):
        f.write(f"{key}: {'; '.join(shows[key])}\n")

# --- Ghi file output_titles.txt ---
# Gom tất cả các tên phim vào 1 list
all_titles = []
for titles in shows.values():
    all_titles.extend(titles)

# Sắp xếp ngược bảng chữ cái (reverse alphabetical order)
all_titles.sort(reverse=True)

with open("output_titles.txt", "w") as f:
    for title in all_titles:
        f.write(f"{title}\n")
