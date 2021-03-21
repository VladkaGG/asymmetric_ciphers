from random import randrange


class RSA:
    p: int = None
    q: int = None

    def __init__(self):
        def getprime(begin, end) -> int:
            def isprime(n):
                x = 2
                while x * x <= n and n % x != 0:
                    x += 1
                return x * x > n

            a = randrange(2 ** begin, 2 ** end)
            while True:
                if isprime(a):
                    return a
                else:
                    a += 1

        self.p = getprime(10, 11)
        self.q = getprime(11, 12)

    def newkeys(self):

        def prime_for(b) -> int:
            def get_nod(x, y) -> int:
                if y == 0:
                    return x
                return get_nod(y, x % y)
            a = b // randrange(2, 5) + 1
            while True:
                if get_nod(b, a) == 1:
                    return a
                a += 1

        def multiple_inv(b, n):
            for i in range(1, n):
                if (i * b) % n == 1:
                    return i
            return 0

        n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        e = prime_for(phi)
        d = 0
        while d == 0:
            d = multiple_inv(e, phi)
            if d == 0:
                e = prime_for(phi)
        return {'e': e, 'n': n}, {'d': d, 'n': n}

    @staticmethod
    def _powmod(a, b, n):
        c = 1
        for _ in range(1, b+1):
            c = (a * c) % n
        return c

    def encrypt(self, message, pub_key):
        return self._powmod(message, pub_key['e'], pub_key['n'])

    def decrypt(self, cihpertext, priv_key):
        return self._powmod(cihpertext, priv_key['d'], priv_key['n'])

def main():
    message = 132
    a = RSA()
    public_key, private_key = a.newkeys()
    print(public_key, private_key)
    cipher = a.encrypt(message, public_key)
    print(cipher)
    print(a.decrypt(cipher, private_key))


if __name__ == "__main__":
    main()
