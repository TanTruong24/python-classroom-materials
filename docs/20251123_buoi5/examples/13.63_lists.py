"""
13.63 PRACTICE: Lists***: Grouping into ranges
A publisher may allow a reader to select a subset of chapters to purchase. 
Given 15 integers that are 0 or 1 indicating whether or not to include chapters 1 to 15, 
output the selection using shorthand for ranges of 3 or more (11, 12, 13 becomes 11-13).

If the input is

1 1 1 1 0 1 0 1 1 0 1 1 1 0 0

the output should be:
1-4 6 8 9 11-13  

If no chapters are selected, output: "None"
For simplicity, follow every term including the last by one space (and end with newline).
"""

num_str = input()
nums = list(map(int, num_str.split()))

count_chapter = 0
start_index = 0
results = []
for i in range(15):
    if nums[i] == 1:
        if count_chapter == 0:
            start_index = i
        count_chapter += 1
    else:
        if count_chapter > 0:
            start_chapter = start_index + 1
            end_chapter = start_index + count_chapter

            if count_chapter == 1:
                results.append(f"{start_chapter}")
            elif count_chapter == 2:
                results.append(f"{start_chapter}")
                results.append(f"{start_chapter + 1}")
            else:
                results.append(f"{start_chapter}-{end_chapter}")
        
        count_chapter = 0
        start_index = None

if len(results) == 0:
    print("None")
else:
    print(" ".join(results), end=" \n")
            