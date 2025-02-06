#Program 8
def power_of_two(n):
  powers = [2 ** i for i in range(1, n+1)]
  return powers

print(power_of_two(6))