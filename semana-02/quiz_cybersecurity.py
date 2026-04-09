# Projeto 3: Quiz de Cybersecurity
# 5 perguntas sobre segurança da informação com placar

perguntas = [
    {
        "pergunta": "O que significa a sigla 'VPN'?",
        "opcoes": ["1 - Virtual Private Network", "2 - Virus Protection Node", "3 - Virtual Public Network", "4 - Verified Private Node"],
        "resposta": "1"
    },
    {
        "pergunta": "Qual ataque engana o usuário para revelar senhas se passando por uma entidade confiável?",
        "opcoes": ["1 - Ransomware", "2 - DDoS", "3 - Phishing", "4 - Keylogger"],
        "resposta": "3"
    },
    {
        "pergunta": "O que é autenticação de dois fatores (2FA)?",
        "opcoes": ["1 - Usar duas senhas diferentes", "2 - Confirmar identidade com dois métodos distintos", "3 - Ter duas contas no sistema", "4 - Fazer login duas vezes"],
        "resposta": "2"
    },
    {
        "pergunta": "Qual protocolo garante que um site é seguro e criptografado?",
        "opcoes": ["1 - HTTP", "2 - FTP", "3 - HTTPS", "4 - SMTP"],
        "resposta": "3"
    },
    {
        "pergunta": "O que faz um ataque de força bruta?",
        "opcoes": ["1 - Invade fisicamente um servidor", "2 - Testa todas as combinações possíveis de senha", "3 - Sobrecarrega um servidor com requisições", "4 - Intercepta dados na rede"],
        "resposta": "2"
    }
]

print("=== QUIZ DE CYBERSECURITY ===")
print(f"Total de perguntas: {len(perguntas)}")

pontos = 0

for i, q in enumerate(perguntas, start=1):
    print(f"\nPergunta {i}: {q['pergunta']}")
    for opcao in q["opcoes"]:
        print(f"  {opcao}")
    print()

    resposta = input("Sua resposta (1, 2, 3 ou 4): ").strip()

    if resposta == q["resposta"]:
        print("Correto!")
        pontos += 1
    else:
        opcao_certa = q["opcoes"][int(q["resposta"]) - 1]
        print(f"Errado! A resposta correta era: {opcao_certa}")

print("\n=============================")
print(f"Resultado: {pontos} de {len(perguntas)} acertos")

if pontos == len(perguntas):
    print("Perfeito! Você é um expert em Cybersecurity!")
elif pontos >= 3:
    print("Muito bem! Continue estudando!")
else:
    print("Continue praticando! Você vai melhorar!")
print("=============================")
