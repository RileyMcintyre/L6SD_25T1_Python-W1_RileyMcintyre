#Program 9
def count_vowels(word):
  vowels = "aeiou"
  count = 0
  for char in word:
    if char.lower() in vowels:
     count += 1
  return count

print(count_vowels("cheese"))