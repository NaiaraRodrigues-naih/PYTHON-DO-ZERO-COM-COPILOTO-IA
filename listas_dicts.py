#lista de materiais escolares
materiais = ["Caderno", "Lápis de cor", "Borracha", "Caneta", "Régua",'Mochila', "Giz de cera"]
materiais.append("Tesoura")
print(materiais)
quantidade_materiais = len(materiais)
print("Quantidade de materiais escolares: 2 de cada ")
#dicionário de informações pessoais
informacoes_pessoais = {
    "nome": "Naiara",
    "sobrenome": "Rodrigues",
    "idade": 30,
    "cidade": "Minas Gerais"
}
print(informacoes_pessoais)
print("Nome: " + informacoes_pessoais["nome"])
print("Sobrenome: " + informacoes_pessoais["sobrenome"])
print("Idade: " + str(informacoes_pessoais["idade"]))
print("Cidade: " + informacoes_pessoais["cidade"])

# Lista de ferramentas de cibersegurança
ferramentas_cyber = ["Nmap", "Wireshark", "Metasploit", "Burp Suite", "John the Ripper"]
print(ferramentas_cyber)
quantidade_ferramentas = len(ferramentas_cyber)
print("Quantidade de ferramentas de cyber: " + str(quantidade_ferramentas))
