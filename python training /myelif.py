#if we have multiple conditions then if else wont work for us
#It picks the First true one and ignores the other elifs 
#find the grade of the mark belowe using the belowe table
# >=70 -A
# <70 AND >=60 -B
# <60 AND >=50 -C
# <50 AND >=49 -D
# <40 -E

marks=70

if marks >= 70:
    print("A")
elif marks < 70 and marks >=60:
    print("B")
elif marks <60 and marks >= 50:
    print("C")
elif marks <50 and marks >= 40:
    print("D")
elif marks < 40:
    print("E")