"""
13.61 PRACTICE: Lists**: Reverse in place
Reversing a list is a common task. One approach copies to a second list in reverse, then copies the second list back to the first. 
However, to save space, reversing a list without using a second list is sometimes preferable. 
Write a function that reverses a given list, without using a second list. 
The program's input is the length of the list, followed by the list itself.

Ex: If the input is
4
2
5
9
7
The output is
7 9 5 2 5 7

Hints:
Use this approach: Swap the first and last elements, then swap the second and second-to-last elements, etc.
Stop when you reach the middle; else, you'll reverse the list twice, ending with the original order.
Think about the case when the number of elements is even, and when odd. Make sure your code handles both cases.
"""
def swap_reverse(nums, length):
    middle_idx = length // 2
    left_idx = 0
    right_idx = length-1
    while True:
        if length % 2 == 0 and left_idx == middle_idx:
            break

        elif length % 2 != 0 and left_idx == right_idx:
            break

        temp = nums[left_idx]
        nums[left_idx] = nums[right_idx]
        nums[right_idx] = temp

        left_idx += 1
        right_idx -= 1

    # Optimal:
    # left = 0
    # right = length - 1
    # while left < right:
    #     nums[left], nums[right] = nums[right], nums[left]
    #     left += 1
    #     right -= 1

    return nums


if __name__ == "__main__":
    n = int(input())
    nums= []
    for _ in range(n):
        nums.append(input())

    nums_copy = nums.copy()

    length = len(nums)
    if length == 0:
        print("Empty")
        
    else:
        # approach 1:
        reversed_nums = swap_reverse(nums, length)
        print (f"approach 1: {" ".join(reversed_nums)}")


    # approach 2: This method creates a new list that contains the elements of the original list in reverse order.
    rev_nums = nums_copy[::-1]
    print(f"approach 2: {" ".join(rev_nums)}")

    # approach 3: This method modifies the original list and does not return a new list
    nums_copy.reverse()
    print(f"approach 3: {" ".join(nums_copy)}")