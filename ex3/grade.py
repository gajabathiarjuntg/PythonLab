def grade(m1,m2,m3):

   total = m1+m2+m3
   average = total/3

   print("Total = ",total)
   print("Average = ",average)

   return 0

n1 = int(input("Enter First subject mark : "))
n2 = int(input("Enter Second subject mark : "))
n3 = int(input("Enter Third subject mark : "))

grade(n1,n2,n3)