#Program 1
#with each iteration of the loop it changes the value in num then adds it to the total 
def calculate_average(numbers):
  total = 0
  for num in numbers:
     total += num
#it then divides the value of total by the amount of values in numbers
  average = total / len(numbers)
  return average
#example + printing the function
numbers = (86 , 72 , 76 , 42)
print(calculate_average(numbers))  

