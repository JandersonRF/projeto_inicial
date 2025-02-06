CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome :")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite valor do seu salario :"))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bonus :"))

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario * bonus_usuario


# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"O usuário {nome} possui o bonûs de {valor_do_bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?


