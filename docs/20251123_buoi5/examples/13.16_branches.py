"""
13.16.1: PRACTICE: Branches**: 24-hour time

24-hour time (also known in the U.S. as military time) is widely used around the world. 
Time is expressed as hours since midnight. 
The day starts at 00:00, and ends at 23:59. Write a program that converts am/pm time to 24-hour time. 
The input is two numbers and a string.

If the input is
2 
30 
pm

the output should be "14:30".

If the input is
12 
01
am

the output should be "00:01".

Hints:
- Think of how each hour should be handled.
    12:00am to 12:59am becomes what? 8:00am becomes what? 12:00 pm? 1:00pm? 
    Group the hours into cases that should be handled similarly (e.g. 1:00am to 11:00am are handled the same).
- Declare variables for hour_am_pm, min_am_pm, and hour_24. 
    Note that minutes for 24-hour time remain the same as for am/pm, so no extra variable is needed.
- Use an if-else statement to detect each case, and set the hour_24 appropriately.
- When outputting hour_24, check if the hour is 0-9 (just check for < 10). 
    If so, output a "0". So 7 will be output as "07". Do the same when outputting the minutes.
"""

input_hour = int(input())
input_minute = input()
input_period = input().strip().lower()

# Cách 1:
dict_hours = {
    "am": {
        12: "00", 1: "01", 2: "02", 3: "03", 4: "04", 5: "05", 6: "06", 7: "07", 8: "08", 9: "09", 10: "10", 11: "11"
    },
    "pm": {
        12: "12", 1: "13", 2: "14", 3: "15", 4: "16", 5: "17", 6: "18", 7: "19", 8: "20", 9: "21", 10: "22", 11: "23"
    }
}
hour_24 = dict_hours[input_period][input_hour]
print(f"{hour_24}:{input_minute}")

# cách 2: theo hints branches

if input_period == 'am':
    if input_hour == 12:
        hour_24_v2 = "00"
    else:
        hour_24_v2 = f"0{input_hour}"
else:
    if input_hour == 12:
        hour_24_v2 = "12"
    else:
        hour_24_v2 = str(12 + input_hour)

print(f"{hour_24_v2}:{input_minute}")