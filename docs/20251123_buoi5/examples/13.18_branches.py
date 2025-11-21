"""
13.18 PRACTICE: Branches**: Runway headings
Airport runways are numbered using a 2-digit number, like 09. 
The meaning generally is that planes taking off or landing on that runway will be facing a number of degrees rotated right from north, 
with the ending 0 left out (Ex. 09 is 90 degrees, 27 is 270 degrees). 
A runway numbered 09 is facing 90 degrees right from north, namely facing east.
Given a runway number (integer), output the degrees followed by the closest direction indication 
(north, northeast, east, southeast, south, southwest, west, or northwest). If the input is 03, the output is: 30 degrees (northeast).

Hints:
- First just read the input number, multiply by 10 to yield runway_deg.
- Next, create an if-else statement to compare runwayDeg's value with ranges for each direction. 
    For north, the value should be within -22.5 and +22.5. For northeast, the value should be between 45 - 22.5 and 45 + 22.5. And so on.
- Based on the range in which the value falls, update a string variable with the direction. 
    Then after the if-else, have a single output statement that outputs "270 degrees (north)" or whatever value and direction are correct.
- Don't forget that ranges use &. An expression detecting a value x is between 1 and 10 is (x > 1) & (x < 10).
- Because the input is an integer which is multiplied by 10 to yield runway_deg, 
    the comparisons with floating-point values like 22.5 will never result in equality. Hence, the ranges don't have to account for such quality.


"""


runway_deg = int(input()) * 10


if 337.5 < runway_deg or runway_deg < 22.5:
    direction = "north"

elif 22.5 < runway_deg < 67.5:
    direction = "northeast"

elif 67.5 < runway_deg < 112.5:
    direction = "east"

elif 112.5 < runway_deg < 157.5:
    direction = "southeast"

elif 157.5 < runway_deg < 205.5:
    direction = "south"

elif 205.5 < runway_deg < 247.5:
    direction = "southwest"

elif 247.5 < runway_deg < 292.5:
    direction = "west"

elif 292.5 < runway_deg < 337.5:
    direction = "northwest"

print(f"{runway_deg} degrees {direction}")