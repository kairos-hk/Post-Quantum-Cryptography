import numpy as np
from numpy.polynomial import polynomial as poly

def generate_polynomial(n, d):
  
    coeffs = [0] * n
    pos_indices = np.random.choice(n, d, replace=False)
    neg_indices = np.random.choice(n, d, replace=False)
    for pos in pos_indices:
        coeffs[pos] = 1
    for neg in neg_indices:
        coeffs[neg] = -1
    return np.array(coeffs)

    for k in range(1, q):
        if np.all((poly.polymul(f, [k]) % q) % n == [1] + [0]*(n-1)):
            return (f * k) % q
    return None

def key_generation(n=7, p=3, q=128, d=2):
    f = generate_polynomial(n, d) + [1]  # f = 1 + xF
    g = generate_polynomial(n, d)
    h = poly.polymul(invert_polynomial(f, n, p), g) % q
    return (f, g, h)

def encrypt(message, h, q=128):

    m = np.array([int(bit) for bit in message])
    e = poly.polymul(m, h) % q
    return e

def decrypt(ciphertext, f, p, q=128, n=7):

    a = poly.polymul(ciphertext, f) % q
    decrypted = np.round((a % p) / p) % 2
    return ''.join(decrypted.astype(int).astype(str))

n, p, q, d = 11, 3, 128, 5
f, g, h = key_generation(n, p, q, d)

message = '1010101'

ciphertext = encrypt(message, h, q)


decrypted_message = decrypt(ciphertext, f, p, q, n)

print(f"Original message: {message}")
print(f"Decrypted message: {decrypted_message}")
