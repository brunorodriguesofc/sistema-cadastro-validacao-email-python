#Sistema de cadastro e Validação de Email

nome = "  bruno rodrigues dos santos  "
email = "  CONTATO2024@GMAIL.COM  "
faturamento = 2500
custo = 1200

# Tratamento
nome = nome.strip().lower().title()
email = email.strip().lower()

# Extração
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]


# Validação
if "@" in email:
    status_email = "Email válido"
    posicao_email = email.find("@")
    servidor = email[posicao_email + 1:]
else:
    status_email = "Email inválido"
    servidor = ""

# Financeiro
lucro = faturamento - custo
margem_lucro = lucro / faturamento

# Classificação
if margem_lucro >= 0.30:
    classificacao = "Alta performance"
elif margem_lucro >= 0.10:
    classificacao = "Média performance"
else:
    classificacao = "Baixa performance"

# Saída final
print(f"Usuário {primeiro_nome} cadastrado com sucesso")
print(status_email)
print(f"Servidor: {servidor}")
print()
print(f"Faturamento: R${faturamento:,.2f}")
print(f"Custo: R${custo:,.2f}")
print(f"Lucro: R${lucro:,.2f}")
print(f"Margem: {margem_lucro:.2%}")
print()
print(f"Classificação: {classificacao}")
