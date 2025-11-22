# 13.24 PRACTICE: Loops*: Password requirements
# Yêu cầu kiểm tra:
# - Ít nhất 8 ký tự
# - Có ít nhất 1 chữ cái
# - Có ít nhất 1 số
# - Có ít nhất 1 ký tự đặc biệt trong nhóm: ! # %

pwd = input()

has_letter = False
has_number = False
has_special = False

for ch in pwd:
    if ch.isalpha():
        has_letter = True
    elif ch.isdigit():
        has_number = True
    elif ch in "!#%":
        has_special = True

errors = []

if len(pwd) < 8:
    errors.append("Too short")
if not has_letter:
    errors.append("Missing letter")
if not has_number:
    errors.append("Missing number")
if not has_special:
    errors.append("Missing special")

if len(errors) == 0:
    print("OK")
else:
    for msg in errors:
        print(msg)


# Test:
# Input:
# Hello
# Output:
# Too short
# Missing number
# Missing special
