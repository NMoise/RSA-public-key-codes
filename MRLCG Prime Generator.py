# LCG Large Prime Generator
import time, random, math
start_time = time.time()    #time Counter

# Key size
n_bits = 16

# Pre prime sieved primes for prime candidates selection
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 
                    79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 
                    167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 
                    257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349]

# n-digits = n-bits * log(2); m = (2**(n-bits + 1)) + k ,m is a constant nearest prime
if n_bits == 4096:
    n_digits, m, Gap = 1234, (2**4097 + 51), 708
elif n_bits == 2048:
    n_digits, m, Gap = 617, (2**2049 + 227), 356
elif n_bits == 1024:
    n_digits, m, Gap = 309, (2**1025 + 1481), 178
elif n_bits == 512:
    n_digits, m, Gap = 155, (2**513 + 159), 89
elif n_bits == 256:
    n_digits, m, Gap = 78, (2**257 + 155), 45
elif n_bits == 128:
    n_digits, m, Gap = 39, (2**129 + 17), 23
elif n_bits == 64:
    n_digits, m, Gap = 20, (2**65 + 131), 12
elif n_bits == 32:
    n_digits, m, Gap = 10, (2**33 + 17), 6
elif n_bits == 16:
    n_digits, m, Gap = 5, (2**17 + 29), 3
    

P1  = 4 * 10**(n_digits - 1) + 1    #P1 is a variable
X0  = (2**(n_bits - 1)) + 7         #Xo = (2^(n-bits - 1)) + k  is the seed and it's value can change too 
P2  = (10**(n_digits - 1)) + 7      #(10^(n-digits - 1)) + k , P2 is an odd variable number

# Strong primality test                   
def miller_rabin(n):
    r, s, k = 0, n - 1, 20
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def gen_linear(a, seed,c, m):
    x=seed
    iteration = 0
    s = []
    #LCG while loop cycle until generated ten prime candidates
    while True:
        Xn = (P1 * x + P2) % m
        x = Xn;
        if Xn % 2 != 0: # Check odd prime candidates
            for divisor in first_primes_list:
                if Xn % divisor == 0:
                    break
            else:
                s.append(Xn)
                iteration += 1
        if iteration == Gap:  #Stop after a specified number of prime candidates depends on our proposed gap lemma.
            break
    return s

res = gen_linear(P1, X0, P2, m)
Prime_rand_list = []

# Test all prime candidates
for i in range(len(res)):
    n = res[i]
    if miller_rabin(n):
        Prime_rand_list.append(n)
        i += 1
print("we got and checked %s Random Prime candidates numbers" % len(res))
print("we got %s Real Random Prime numbers" % len(Prime_rand_list))
#print("Random Prime candidates numbers are: %s " % res)
print("Real Prime Random numbers are: %s " % Prime_rand_list)
print("Execution Time %s seconds ---" % (time.time() - start_time)) #Execution