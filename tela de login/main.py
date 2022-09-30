from login import Login

name = Login()
# name.cadastro()

print("digite 1 para login e 2 para cadastrar: ")

opcao = int(input(""))
if opcao == 1:
    name.login()
    
if opcao == 2:
    name.cadastro()