<<<<<<< HEAD
def gcd(a, b):

    if (a == 0):
        return b
    return gcd(b % a, a)


def phi(n):

    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result


for n in range(1, 11):
    print("phi(",n,") = ", 
           phi(n), sep = "")
           

=======
def gcd(a, b):

    if (a == 0):
        return b
    return gcd(b % a, a)


def phi(n):

    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result


for n in range(1, 11):
    print("phi(",n,") = ", 
           phi(n), sep = "")
           

>>>>>>> 3c6f368b43776c615a9aa893eb128b7c8bb1c3c6
