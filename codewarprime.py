def is_prime(num):
  n = 3
  isPrime = False
  while True:
    for n in range(1, num/3, 2)
        if num == 1:
            isPrime = False
            break
        if num == 2:
            isPrime = True
            break
        if num <= 0:
            isPrime = False
            break
        remainder = num % n
        if remainder == 0:
              isPrime = False
              break
        elif remainder != 0:
              n = n + 2
              continue
    if isPrime == False:
        return False
    if isPrime == True:
        return True
        
print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(73))
print(is_prime(75))
print(is_prime(-1))

print(is_prime(3))
print(is_prime(5))
print(is_prime(7))
print(is_prime(41))
print(is_prime(5099))

print(is_prime(4))
print(is_prime(6))
print(is_prime(8))
print(is_prime(9))
print(is_prime(45))
print(is_prime(-5))
print(is_prime(-8))
print(is_prime(-41))

