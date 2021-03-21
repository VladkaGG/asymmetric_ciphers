from random import randint


class ElGamal:
    def __init__(self):
        pass

    @staticmethod
    def _pow_mod(a, b, n):
        c = 1
        for i in range(1, b + 1):
            c = (c * a) % n
        return c

    def generate(self, _from, to):
        def prim_root(m):
            def nod(x, y):
                if y == 0: return x
                return nod(y, x % y)

            all_group = set(x for x in range(1, m))
            for i in range(1, m):
                round_set = set(self._pow_mod(i, powers, m) for powers in range(1, m))
                if round_set == all_group:
                    return i

        def get_prim(begin, end):
            def is_prim(num):
                if num % 2 == 0: return False
                for x in range(3, num // 2, 2):
                    if num % x == 0: return False
                return True
            prim = randint(10**begin, 10**end)
            while not is_prim(prim):
                prim = randint(10**begin, 10**end)
            return prim

        p = get_prim(_from, to)
        g = prim_root(p)
        x = randint(1, p-1)
        y = self._pow_mod(g, x, p)
        return {'key': y, 'p': p, 'g': g}, {'key': x, 'p': p}

    def encrypt(self, message, pub_key):
        k = randint(1, pub_key['p'] - 2)
        a = self._pow_mod(pub_key['g'], k, pub_key['p'])
        b = (self._pow_mod(pub_key['key'], k, pub_key['p']) * message) % pub_key['p']
        return {'a': a, 'b': b}

    def decrypt(self, ciph, priv_key):
        return (ciph['b'] * self._pow_mod(ciph['a'], priv_key['p'] - 1 - priv_key['key'], priv_key['p'])) % priv_key['p']

def main():
    message = 11
    public, private = ElGamal().generate(3, 4)
    cipher = ElGamal().encrypt(message, public)
    print(cipher)
    print(ElGamal().decrypt(cipher, private))


if __name__ == '__main__':
    main()
