#Program 4
def is_prime(n):
    prime = True
    if n < 2 :
       return False
    for i in range(2, n):
        if n % i == 0:
          prime = False
        return prime
    
print(is_prime(4))
print(is_prime(5))
print(is_prime(1))
