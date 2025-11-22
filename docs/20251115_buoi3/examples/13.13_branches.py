# 13.13 PRACTICE: Branches*: Listing names
# Input: 6 words = first1 last1 first2 last2 first3 last3
# last may be "none". Output theo quy tắc:
# - Không ai tồn tại → "TBD"
# - 1 người → "F. Last"
# - 2 người → "Last1 / Last2"
# - 3 người → "Last1 / Last2 / ..."

f1 = input()
l1 = input()
f2 = input() 
l2 = input()
f3 = input()
l3 = input()

exists1 = (f1 != "none")
exists2 = (f2 != "none")
exists3 = (f3 != "none")

count = exists1 + exists2 + exists3


if count == 0:
    print("TBD")
elif count == 1:
    # chỉ người 1
    if exists1:
        print(f"{f1[0]}. {l1}")
    elif exists2:
        print(f"{f2[0]}. {l2}")
    else:
        print(f"{f3[0]}. {l3}")
elif count == 2:
    names = []
    if exists1: names.append(l1)
    if exists2: names.append(l2)
    if exists3: names.append(l3)
    print(f"{names[0]} / {names[1]}")
else:  # count == 3
    print(f"{l1} / {l2} / ...")


# Test:
# Input:
# Ann Jones none none none none
# Output:
# A. Jones
#
# Input:
# Ann Jones Mike Smith none none
# Output:
# Jones / Smith
#
# Input:
# Ann Jones Mike Smith Lee Nguyen
# Output:
# Jones / Smith / ...
