class Login:
    def cadastro(nome):
        lista = ["luiz", "eu"]
        nome = input("digite seu nome('break' para parar e 'logar' para login): ")

        while nome != "break" and nome != "logar":
            lista.append(nome)
            print(lista)
            nome = input("digite seu nome('break' para parar e 'logar' para login): ")

        if nome == "break":
            print("acabou!")

        if nome == "logar":
            nome_teste = input("digite seu nome: ")
            for i in lista:
                if nome_teste == nome:
                    print("login completo")
                else:
                    print("usuario nao encontrado")

    def login(nome_teste, nome, lista):
        nome_teste = input("digite seu nome: ")
        for i in lista:
            if nome_teste == nome:
                print("login completo")
            else:
                print("usuario nao encontrado")
        