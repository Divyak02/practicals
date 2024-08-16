prime = int(input("Enter the prime number: "))
primitive = int(input("Enter the primiitve root: "))
xa = int(input("Enter the value of Xa: "))
xb = int(input("Enter the value of Xb: "))

def deffie_hellman(prime, primitive, xa, xb):
    ya = pow(primitive, xa, prime)
    yb = pow(primitive, xb, prime)
    priv_a = pow(yb, xa, prime)
    priv_b = pow(ya, xb, prime)
    return priv_a, priv_b, ya, yb
    

keys = deffie_hellman(prime, primitive, xa, xb)

print(f"Public Key of A = {keys[2]}")
print(f"Public Key of B = {keys[3]}")
print(f"Private Key of A = {keys[0]}")
print(f"Private Key of B = {keys[1]}")

if keys[0] == keys[1]:
    print("This contains shared private keys")
else:
    print("This doesn't contain shared private keys")

