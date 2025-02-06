#Program 5
def print_pattern(rows):
  for i in range(1, rows + 1):
    for j in range(1, i):
         print(j, end="")
    print()

rows = int(input("rows   "))

print_pattern(rows)