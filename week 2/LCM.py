import sys
input = sys.stdin.readline()


def GCD(a, b):
    if b == 0:
        return a
    else:
        z = a % b

    return GCD(b, z)


a, b = map(int, input.split())
gcd = GCD(a, b)
# actual Formula is HCf(a,b) * LCM(a,b) = a*b
print(int((a/gcd) * b))
