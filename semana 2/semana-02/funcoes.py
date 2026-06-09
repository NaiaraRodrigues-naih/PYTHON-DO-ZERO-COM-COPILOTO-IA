# criando uma funcão
def saudacao():
    print("Olá! Bem-vindo ao curso de Python para Iniciantes.")
# chamando a função
saudacao()
print("Função chamada com VENCEDOR!")
# função com parâmetros
def saudacao_personalizada(nome):
    print("Olá, " + nome + "! Bem-vindo ao curso de Python para Iniciantes.")
saudacao_personalizada("Naiara")
# função com múltiplos parâmetros
def saudacao_com_idade(nome, idade):
    print("Olá, " + nome + "! Você tem " + str(idade) + " anos. Bem-vindo ao curso de Python para Iniciantes.")
saudacao_com_idade("Naiara", 30)
# função com retorno
def calcular_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    return idade
idade_calculada = calcular_idade(1996)
print("A idade calculada é: " + str(idade_calculada))
