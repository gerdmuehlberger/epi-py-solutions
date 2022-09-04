from typing import List


def is_prime(n):
    if n > 1:
        if n != 2:
            for i in range(2, int(n/2)+1):
                if n%i == 0:
                    return False
            return True
        else:
            return True
    else:
        return False

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:

    sol = []
    for i in range(2, n+1):
        if is_prime(i):
            sol.append(i)
    return sol