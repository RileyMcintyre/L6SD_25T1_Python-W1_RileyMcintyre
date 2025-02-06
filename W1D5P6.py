#Program 6
def find_max(numbers):
  max_num = numbers [0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num
    
print(find_max([5 ,5 ,5 ,5]))

