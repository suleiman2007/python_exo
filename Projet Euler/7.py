y = 1
counter = 0
ist = False


def is_prime(x):
    global ist
    s = 0
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            s += 1
    if s == 0:
        ist = True


while True:
    y += 1
    is_prime(y)
    if ist is True:
        ist = False
        counter += 1
    if counter == 10001:
        print(y)
        break
