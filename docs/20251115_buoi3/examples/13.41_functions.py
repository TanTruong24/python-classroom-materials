# 13.41 PRACTICE: Functions*: Rotate three values
# Rotate nghĩa là: p1 -> p2, p2 -> p3, p3 -> p1

def rotate_right3(p1, p2, p3):
    tmp = p3
    p3 = p2
    p2 = p1
    p1 = tmp
    return p1, p2, p3

# def rotate(p1, p2, p3):
#     p1, p2, p3 = p3, p1, p2
#     return p1, p2, p3


# Input
n1 = int(input())
n2 = int(input())
n3 = int(input())
   
n1, n2, n3 = rotate_right3(n1, n2, n3)
   
print(n1, n2, n3)


# Test:
# Input:
# 2
# 4
# 6
# Output:
# 6 2 4
