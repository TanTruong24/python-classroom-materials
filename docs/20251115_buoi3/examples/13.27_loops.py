# 13.27 PRACTICE: Loops (while)**: Output rocket height
# Công thức: h = (v_i * t) - (5 * t^2)
# Input: initial velocity (v_i)
# Output: time t và chiều cao h, dừng khi h < 0

v_i = int(input())
t = 0

while True:
    h = (v_i * t) - (5 * t * t)
    if h < 0:
        break
    print(t, h)
    t += 1


# Test:
# Input:
# 20
# Output:
# 0 0
# 1 15
# 2 20
# 3 15
# 4 0
