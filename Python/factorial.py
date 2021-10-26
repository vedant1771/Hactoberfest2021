#code to get factorial of a number
def print_factors(x):
       print("The factors of",x,"are:")
       for i in range(1, x + 1):
           if x % i == 0:
               print(i)
num=int(input())
print_factors(num)
