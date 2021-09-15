import math
print("enter the lengths of the room")
x = float(input()) 
y = float(input())

print("enter the height")# me not assuming the room is square-shaped
h = float(input())

d1 = float(x * h)
d2 = float(y * h)
dt = 2*(d1 + d2)

n = 2
uptt = 0
while bool(n) == True:
    if n == 2:
        print("enter diementions of any doors, windwos or other unpaintable areas")
    if n == 1:
        print("enter diementions of any other doors, windwos or other unpaintable areas")
    up1 = int(input())
    up2 = int(input())
    upt = int(up1 * up2)
    uptt = int(uptt + upt)
    print("is there any other unpaintable area? enter: 1 for yes & 0 for no")
    n = int(input())
tt = str(dt - uptt)
itt = int(dt - uptt)
print (tt + "litres of paint requiring " + str(math.ceil(itt)))