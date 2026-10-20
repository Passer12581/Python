import sys
import bisect
def sieve(limit):
    is_prime = [True]*(limit+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2,int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,limit+1,i):
                is_prime[j] = False
    primes = [x for x,flag in enumerate(is_prime) if flag]
    return primes
max_n = 10**8
primes = sieve(10000)
all_vals = set()
for c in primes:
    c4 = c**4
    if c4 > max_n:
        break
    for b in primes:
        b3 = b**3
        sum_bc = c4 + b3
        if sum_bc > max_n:
            break
        for a in primes:
            a2 = a**2
            total = a2 + sum_bc
            if total > max_n:
                break
            all_vals.add(total)
sorted_nums = sorted(all_vals)
def main():
    t = int(input())
    out = []
    for _ in range(t):
        n = int(input())
        out.append(str(bisect.bisect_right(sorted_nums, n)))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
