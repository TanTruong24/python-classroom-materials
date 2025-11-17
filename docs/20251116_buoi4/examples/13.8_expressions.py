"""
13.8 PRACTICE: Expressions* Phone numbers
Formatting makes text easier for the viewer to read. Given a 10-digit phone number, output the number in a format that is easier for a person to read.

Ex: If the input is:

1234567890
the output should be:

(123) 456-7890
"""

phone_number = input()

formatted_number = f"({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:10]}"
print(formatted_number)