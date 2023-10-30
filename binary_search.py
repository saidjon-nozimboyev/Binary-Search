key = int(input("Please enter a number: "))
left = 0
right = 10**9
while left <= right:
    md = (left + right) // 2
    if md < key:
        left = md + 1
    elif md == key:
        print(f"Enteres number is: {md}")
        break
    else:
        right = md - 1