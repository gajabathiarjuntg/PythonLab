def circle(r):

   area = 3.14 * r * r
   return area

def rectangle(length,breadth):

   area = length * breadth
   return area

r = int(input("Enter Radius : "))
l = int(input("Enter Length : "))
b = int(input("Enter Breadth : "))

print("Area of Circle is ",circle(r))
print("Area of Rectangle is ",rectangle(l,b))