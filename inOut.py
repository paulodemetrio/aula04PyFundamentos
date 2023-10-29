if __name__ == "__main__":
    # arquivo = open('lang.txt')
    # print(arquivo.read()) 
    # arquivo.close()

    with open('lang.txt') as arquivo:
        print(arquivo.readlines(10))
        arquivo.seek(0)
        print(arquivo.readlines(30))