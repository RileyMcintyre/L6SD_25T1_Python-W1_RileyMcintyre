#Program 10
def find_average(nums):
  total = 0
  count = 0
  for num in nums:
     total += num
     count += 1
  average = total / count
  return average

print(find_average([5 , 6, 2 , 1 , 6]))