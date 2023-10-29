def fatorial(n):
    cont = n
    total = n
    while cont > 1:
        total = total * (cont - 1)
        cont = cont -1
    return total

if __name__ == '__main__':
    print(fatorial(10))