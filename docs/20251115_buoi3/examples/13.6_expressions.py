"""
13.6 PRACTICE: Expressions*: Simple floating-point expression

Đề bài:
Write an assignment statement for the following mathematical equation:

    y = (1/3)x + (x/4) + 2x

Keep x as an integer. Use an expression that matches the equation's right side
as closely as possible. If the input is -1, the output is -2.58333.
"""

x = int(input())
y = (1.0 / 3) * x + (x / 4.0) + 2 * x
print(y)


# ===== MỘT SỐ TEST CASE THAM KHẢO (CHẠY THỰC TẾ) =====
#
# Test case 1:
# Input:
# -1
#
# Output (chương trình in ra xấp xỉ):
# -2.583333333333333
#
# Trong hệ thống chấm tự động họ sẽ chỉ so sánh đến 5 chữ số sau dấu phẩy:
# -2.58333  ✔
#
# --------------------------------------------
# Test case 2:
# Input:
# 0
#
# y = (1/3)*0 + 0/4 + 2*0 = 0
#
# Output:
# 0.0
#
# --------------------------------------------
# Test case 3:
# Input:
# 4
#
# y = (1/3)*4 + 4/4 + 2*4
#   = 4/3 + 1 + 8
#   = 1.33333... + 1 + 8
#   = 10.33333...
#
# Output (xấp xỉ):
# 10.333333333333334
#
# --------------------------------------------
# Test case 4:
# Input:
# 1
#
# y = (1/3)*1 + 1/4 + 2*1
#   = 1/3 + 1/4 + 2
#   = 0.33333... + 0.25 + 2
#   = 2.58333...
#
# Output (xấp xỉ):
# 2.583333333333333
#