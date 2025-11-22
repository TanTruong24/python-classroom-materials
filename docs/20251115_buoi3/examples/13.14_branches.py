passenger_age = int(input())
carry_ons = int(input())
checked_bags = int(input())

# 13.14 PRACTICE: Branches**: Complex cost structure
# Input (mỗi dòng): age, carry_on(0/1), checked_bags(>=0)
# Output: tổng tiền vé (air_fare)

age = int(input())
carry_on = int(input())
checked_bags = int(input())

if age <= 2:
    air_fare = 0
elif age >= 60:
    air_fare = 290
else:
    air_fare = 300

# Carry-on
if carry_on == 1:
    air_fare += 10


if checked_bags == 2:
    air_fare += 25
else:
    air_fare += 25 + (checked_bags - 2) * 50

print(air_fare)

# Ví dụ test:
# Input:
# 30
# 1
# 3
# Tính: base 300 + carry_on 10 + (25 + 1*50) = 385
# Output:
# 385
