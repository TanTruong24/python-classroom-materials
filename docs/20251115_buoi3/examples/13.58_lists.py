# 13.58 PRACTICE: Lists**: Min, max, average
# Input: 10 số nguyên
# Output: min, max, average (average dùng chia 10.0 để ra float)

user_values = [None] * 10
   
for i in range(10):
    use_values[i] = int(input())

for n in user_values:
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n
    sum_val += n

avg = sum_val / 10.0

print(min_val, max_val, avg)


# Test:
# Input:
# 1 1 1 1 3 3 3 3 3 3
# Output:
# 1 3 2.0
#
# Input:
# 9 8 7 6 5 4 3 2 1 0
# Output:
# 0 9 4.5

#optimal
# 
# nums = list(map(int, input().split()))

# minimum = min(nums)
# maximum = max(nums)
# average = sum(nums) / 10.0

# print(minimum, maximum, average)