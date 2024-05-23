from typing import List
def prime_factors()->List[int]:
    '''returns the prime factors of n'''
    num = 2
    n = int(input('Enter no to factorize: '))
    factors = []
    while num*num <= n:
        if n % num:
            num +=1
        else:
            n //=num
            factors.append(num)
    if n > 1:
        factors.append(n)

    return factors

def main():
    print(prime_factors())
if __name__ == '__main__':
    main()
