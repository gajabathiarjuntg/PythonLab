def calc(a,b,choice):

   if(choice==1):
      return a+b
   elif(choice==2):
      return a-b
   elif(choice==3):
      return a*b
   elif(choice==4):
      return a/b

   return 0

a = int(input("Enter a Number : "))
b = int(input("Enter a Number : "))

print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter your Choice : "))

print(calc(a,b,choice))