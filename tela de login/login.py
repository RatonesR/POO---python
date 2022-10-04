class Login:
    def cadastro(nome):
        lista = ["luiz", "eu"]
        nome = input("digite seu nome para cadastrar('break' para parar e 'logar' para login): ")

        while nome != "break" and nome != "logar":
            lista.append(nome)
            print(lista)
            nome = input("digite seu nome('break' para parar e 'logar' para login): ")

        if nome == "break":
            print("acabou!")

        if nome == "logar":
            nome_teste = input("digite seu nome: ")
            if nome_teste in lista:
                print("login completo")
            else:
                print("falha")

    def login(nome_teste, lista):
        nome_teste2 = input("digite seu nome: ")
        if nome_teste2 in lista:
            print("login completo")
        else:
            print("falhou")