if __name__ == '__main__':
    arquivo = open('y.txt', 'w')
    list_ln = []
    cont = True

    while cont:
        name = input('Informe o nome: ')
        city = input('Informe uma cidade: ')
        sex = input('Informe o sexo(M / F): ')

        conteudo = f"Nome: {name}\nCidade: {city}\nSexo: {sex}\n{'-'*50}\n"
        list_ln.append(conteudo)
        arquivo.write(conteudo)
        print('Registro feito com sucesso!')

        cont = bool(int(input('Deseja inserir outro registro? (1 = SIM) / (0 = NÃO) ')))

    arquivo.close()

    with open('z.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.writelines(list_ln)
