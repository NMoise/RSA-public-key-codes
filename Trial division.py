def trial_division(n: int) -> list[int]:
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1: a.append(n)
    # Only odd number is possible
    return a

# VOID MAIN
if __name__ == "__main__":

    n = 10967535067
    print("One of the divisors for", n , "is ",trial_division(n))