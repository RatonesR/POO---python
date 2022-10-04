from login import Login

name = Login()
# name.cadastro()

print("digite 2 para cadastrar: ")

opcao = int(input())
    
if opcao == 2:
    name.cadastro()
else:
    print("erro")