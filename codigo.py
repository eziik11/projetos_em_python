cpf = input("Qual é o seu CPF? ")
endereco = input("Qual é o seu endereço (rua, número, bairro, cidade)? ")
nome = input("Qual é o seu nome completo? ")
salario = int(input("Qual é o seu salário? "))

# Remove caracteres especiais do CPF
cpf = cpf.replace(".", "").replace("-", "")

# Calcula o primeiro dígito verificador
soma_total = sum(
    int(digito) * peso for digito, peso in zip(cpf[:9], range(10, 1, -1)))
resto = soma_total % 11
primeiro_digito = 0 if resto < 2 else 11 - resto

# Calcula o segundo dígito verificador
soma_total02 = sum(
    int(digito) * peso for digito, peso in zip(cpf[:10], range(11, 1, -1)))
resto02 = soma_total02 % 11
segundo_digito = 0 if resto02 < 2 else 11 - resto02

# Verifica se os dígitos verificadores estão corretos
if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
  print(
      f"Caro, senhor {nome}, locatário de {endereco}, com CPF {cpf}, seu novo salário é {salario}."
  )
else:
  print("CPF inválido. Verifique os dígitos verificadores.")

print(
    f"Caro, senhor: {nome}, locatário de: {endereco}, de CPF: {cpf}, seu salario novo e: {salario}"
)
