# 13.9 PRACTICE: Expressions* Proper name layout
#
# Đề bài:
# Many documents require a specific format for listing a person's name.
# Assume you are given a person's full name (three lines of input: first name,
# middle name, last name). Output the full name in the following format:
#
#       lastName, firstName middleInitial.
#
# Ví dụ:
# Input:
# John
# Jane
# Doe
#
# Output:
# Doe, John J.

first_name = input()
middle_name = input()
last_name = input()

middle_initial = middle_name[0]

result = last_name + ", " + first_name + " " + middle_initial + "."
print(result)

# print(f"{last_name}, {first_name} {middle_name[0]}.")


# ===== TEST CASE THAM KHẢO =====
#
# Test 1:
# Input:
# John
# Jane
# Doe
#
# Output:
# Doe, John J.
# ----------------------------------------
#
# Test 2:
# Input:
# Alice
# Marie
# Johnson
#
# Output:
# Johnson, Alice M.

