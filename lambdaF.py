from random import randint

if __name__ == '__main__':
    list_n = [randint(1,100) for _ in range(1,101)]
    list_pares = list(filter(lambda x: not x % 2 , list_n))
    list_pares.sort()
    print(list_pares)

    
    list_quad = list(map(lambda x: x ** 2, list_pares))
    print(list_quad)
