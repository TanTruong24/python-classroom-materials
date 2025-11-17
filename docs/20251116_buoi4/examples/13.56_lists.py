"""
13.56 PRACTICE: Lists*: Copying only negative values
A list of 6 integers is input into list list_ints. Complete the program to copy only the negative integers to a new list list_neg_ints. 
Output the number of negative elements, and the negatives list. 
Ex: For input
5 
-2 
0 
9 
-66 
-4

the output is:
3
-2
-66
-4

Hints:
Add elements using list_neg_ints.append(â¦)
Write a first for loop that copies only the negative integers to list_neg_ints, then write a second for loop that outputs.
Your copying for loop should have an if statement that only copies the current list_ints element if negative.
The number of items in list_neg_ints can be determined using len(list_neg_ints). No need to have a separate variable keeping track.
"""

list_ints = []
list_neg_ints = []

   
# Get input integers
for i in range(6):
    list_ints.append(int(input()))
    
for num in list_ints:
    if num < 0:
        list_neg_ints.append(num)

print(len(list_neg_ints))
for neg_num in list_neg_ints:
    print(neg_num)
