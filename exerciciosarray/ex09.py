listadenome=[]
listadesenha=[]
print("Olá, vamos efetuar seu cadastro:")
for x in range(5):
    nome=input("Digite seu nome:")
    listadenome.append(nome)
    senha=input("Digite uma senha:")
    listadesenha.append(senha)
print("Agora faça o seu login:")
confirmnome=input("Digite seu nome:")
confirmsenha=input("Digite a sua senha:")
for i in range(5):
    if confirmnome==listadenome[i] and confirmsenha==listadesenha[i]:
        print("Login efetuado com sucesso.")
        break
    else:
        print("Usuário ou senha incorreto")
        break