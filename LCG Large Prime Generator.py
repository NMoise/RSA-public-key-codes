# LCG Large Prime Generator
import time, random, math
start_time = time.time()    #time Counter
# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 
                    79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 
                    167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 
                    257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349]
                    
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
                iteration = iteration + 1
        if iteration == 10:  #Stop after ten prime candidates
            break
    return s

P1  = (4 * 10**3) + 1      #(4 * (10**(n-digits/2)) + 1, P1 is a variable
X0  = (2**15) + 1     #(2^(n-bits - 1)) + 1  
P2  = (2**15) + 7     #(2^(n-bits - 1)) + 7 odd number, P2 is a variable
m   = (2**17) + 29     #(2**(n-bits + 1)) + k nearest prime,m is constant
res = gen_linear(P1, X0, P2, m)
RealPrime = []
for i in range(len(res)):
    n = res[i]
    if miller_rabin(n):
        RealPrime.append(n)
        i += 1
print("Primes candidates are: %s " % res)
print("Real Primes are: %s " % RealPrime)
print("--- %s seconds ---" % (time.time() - start_time)) #Execution time