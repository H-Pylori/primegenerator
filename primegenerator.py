import time

import numpy as np


def prompt_user():
    num_primes = -1
    while num_primes <= 3:
        user_input = input('Please enter a positive integer greater than 3. ')
        try:
            num_primes = int(user_input)
        except ValueError:
            print(f'{user_input} is not a positive integer.')
    return num_primes


def divisible_by(num, divisors):
    divideList = np.array([x for x in divisors if x <= np.sqrt(num)])
    remainders = num % divideList
    return 0 not in remainders


def get_primes(max_num):
    primes = [1, 2]

    for i in range(3, max_num + 1, 2):
        if not divisible_by(i, primes):
            primes.append(i)
    return primes


def main():
    print('How many prime numbers forward would you like to output?')
    user_num = prompt_user()

    start_time = time.time()
    primes = get_primes(user_num)
    end_time = time.time()

    prime_count = len(primes)
    percent_prime = (prime_count / user_num) * 100
    prime_time = (end_time - start_time)
    prime_per_sec = prime_count / prime_time

    print(f'Primes Found:\n\t{primes}')
    print(
        f'Total Prime Numbers: {prime_count}, Percent Prime: {percent_prime:2f}%')
    print(
        f'Time Taken: {prime_time}, Prime/Second: {prime_per_sec}, Final Number Tested: {user_num}')


if __name__ == '__main__':
    main()
