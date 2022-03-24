import random


def euklides(bigger, lesser):   # if those numbers are equal their order doesn't matter
    wynik = bigger % lesser
    if wynik == 0:
        return lesser
    else:
        return euklides(lesser, wynik)


listOfPrimes = [193939, 199933, 319993, 31999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331, 106033, 108301, 112909, 115249, 108881, 110881, 118081, 120121, 121021, 121151, 150151, 151051, 151121, 180181, 180811, 181081]

# p = int(input("Insert first prime number you want to use to cypher message: "))
# q = int(input("Insert second prime number you want to use to cypher message: "))
p = listOfPrimes[random.randrange(0, len(listOfPrimes))]
different = False
while not different:
    q = listOfPrimes[random.randrange(0, len(listOfPrimes))]
    different = p != q

print("Chosen primes are", p, "and", q)


n = p * q
product = (p - 1) * (q - 1)
coPrime = False

while not coPrime:
    e = random.randrange(1, product)
    coPrime = euklides(product, e) == 1

print("e is equal to", e)

symetric = False
d = 0
while not symetric:
    if d % 10000000 == 0:
        print("Looking for d...")
    d += 1
    symetric = (d * e)%product == 1

print("Prime numbers are", p, "and", q, "\b, and so e =", e, "and d =", d, "are symetric mod", product)
print("(e * d) mod product =", (e * d)%product)

print("You are allowed to encrrypt message lower than", n)
message  = int(input("Insert your message: "))
# binaryMessage = ''.join(format(ord(x), 'b') for x in message)
# print(binaryMessage)
encryptedMessage = 1
for i in range(e):
    encryptedMessage = (encryptedMessage * message) % n
print(encryptedMessage)
decryptedMessage = 1
for i in range(d):
    decryptedMessage = (decryptedMessage * encryptedMessage) % n
print(decryptedMessage)