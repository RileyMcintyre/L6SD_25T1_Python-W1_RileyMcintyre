#Program 1
def calculate_average(numbers):
  total = 0
  for num in numbers:
     total += num
  average = total / len(numbers)
  return average
numbers = (86 , 72 , 76 , 42)
print(calculate_average(numbers))  

