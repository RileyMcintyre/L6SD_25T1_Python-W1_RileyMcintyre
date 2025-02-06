#Program 2
 # this show the exaction for the factorial eg it start as 4 it will go 4 * factorial(4-1) then 3 * factorial(3-1) until it reaches 1 then brackes the loop so you would end up with 4*3*2*1
def factorial(n):
 if n == 0 or n == 1:
    return 1
 else:
   return n * factorial(n-1)

#this is a user input and where the total vaule is printed
n = int(input("number    "))
print (factorial(n))
