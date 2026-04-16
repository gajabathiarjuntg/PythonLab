def voting(a):

   if(a>=18):
      print("You are Eligible to Vote")
   else:
      print("You are not Eligible to Vote")
   return 0

age = int(input("Enter Your age : "))

voting(age)