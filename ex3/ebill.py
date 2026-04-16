# Simple Python program to calculate EB Bill
def ebill(units):

   if units <= 100:
      bill = 0
   elif units <= 200:
      bill = (units - 100) * 2
   elif units <= 300:
      bill = (100 * 2) + (units - 200) * 3
   else:
      bill = (100 * 2) + (100 * 3) + (units - 300) * 5

   print(f"Total EB Bill amount : {bill}")


units = int(input("Enter the total units consumed: "))

ebill(units)