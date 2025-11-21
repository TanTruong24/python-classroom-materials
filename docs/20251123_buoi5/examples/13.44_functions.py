"""
13.44 PRACTICE: Functions**: Rideshare pickup time
Rideshare companies like Uber or Lyft track the x,y coordinates of drivers and customers on a map. 
If a customer requests a ride, the company's app estimates the minutes until the nearest driver can arrive. 
Write a function that, given the x and y coordinates of a customer and the three nearest drivers, returns the estimated pickup time. 
Assume drivers can only drive in the x or y directions (not diagonal), and each mile takes 2 minutes to drive. All values are integers.

Hints:

- Break the problem into three parts. In the first part, compute the three distances.
- In the second part, determine the minimum distance. In the third part, compute and return the time.
- Don't forget to use absolute value when computing the x distance, and again for the y distance, because direction doesn't matter. 
    You may wish to just write a small absolute value function.
"""

def calculate_distance(user_x, user_y, x, y):
    return abs(x-user_x) + abs(y-user_y)


# All x, y coordinates are in miles from the origin 0, 0. 
def pickup_minutes(user_x, user_y, d1_x, d1_y, d2_x, d2_y, d3_x, d3_y):
    d1 = calculate_distance(user_x, user_y, d1_x, d1_y)
    d2 = calculate_distance(user_x, user_y, d2_x, d2_y)
    d3 = calculate_distance(user_x, user_y, d3_x, d3_y)

    d_min = min(d1, d2, d3)

    return d_min * 2

user_x = int(input())
user_y = int(input())
d1_x = int(input())
d1_y = int(input())
d2_x = int(input())
d2_y = int(input())
d3_x = int(input())
d3_y = int(input())
   
print(pickup_minutes(user_x, user_y, d1_x, d1_y, d2_x, d2_y, d3_x, d3_y))