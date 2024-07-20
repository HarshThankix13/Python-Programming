# # find first n prime numbers in python code
# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True

#     if num % 2 == 0 or num % 3 == 0:
#         return False

#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6

#     return True

# def find_primes(n):
#     primes = []
#     num = 2
#     while len(primes) < n:
#         if is_prime(num):
#             primes.append(num)
#         num += 1
#     return primes

# n = int(input("Enter the value of n: "))
# prime_numbers = find_primes(n)
# print(f"The first {n} prime numbers are:")
# print(prime_numbers)

# second method 

num = int(input("Enter The Numbers :"))
c =2 
while num!=0:
        for i in range(2,c):
            if c % i == 0:
                break
        else:
            print(c , end= " ")
            num == 1
            c += 1        