"""
Em Python, os sinais de operação são chamados de operadores e são usados para realizar diversas operações em valores e variáveis. Eles são classificados em diferentes categorias, como operadores aritméticos, de comparação, lógicos, de atribuição e bit a bit.

1. Operadores Aritméticos:

Os operadores aritméticos são usados para realizar operações matemáticas básicas:

+: Adição (ex: 5 + 3 = 8)
-: Subtração (ex: 10 - 4 = 6)
*: Multiplicação (ex: 6 * 7 = 42)
/: Divisão (ex: 15 / 3 = 5.0)
//: Divisão inteira (ex: 15 // 3 = 5)
%: Módulo (resto da divisão) (ex: 17 % 5 = 2)
**: Exponenciação (ex: 2 ** 3 = 8)
2. Operadores de Comparação:

Os operadores de comparação são usados para comparar dois valores e retornam um valor booleano (verdadeiro ou falso):

==: Igual (ex: 5 == 5 é verdadeiro)
!=: Diferente (ex: 5 != 3 é verdadeiro)
>: Maior que (ex: 8 > 6 é verdadeiro)
<: Menor que (ex: 2 < 9 é verdadeiro)
>=: Maior ou igual (ex: 7 >= 7 é verdadeiro)
<=: Menor ou igual (ex: 4 <= 5 é verdadeiro)
3. Operadores Lógicos:

Os operadores lógicos são usados para combinar expressões booleanas:

and: E (ex: True and False é falso)
or: Ou (ex: True or False é verdadeiro)
not: Não (ex: not True é falso)
4. Operadores de Atribuição:

Os operadores de atribuição são usados para atribuir valores a variáveis:

=: Atribuição simples (ex: x = 10)
+=: Adição e atribuição (ex: x += 5 é equivalente a x = x + 5)
-=: Subtração e atribuição (ex: x -= 3 é equivalente a x = x - 3)
*=: Multiplicação e atribuição (ex: x *= 2 é equivalente a x = x * 2)
/=: Divisão e atribuição (ex: x /= 4 é equivalente a x = x / 4)
%=: Módulo e atribuição (ex: x %= 3 é equivalente a x = x % 3)
**=: Exponenciação e atribuição (ex: x **= 2 é equivalente a x = x ** 2)
5. Operadores Bit a Bit:

Os operadores bit a bit realizam operações em nível de bit:

&: E bit a bit
|: Ou bit a bit
^: Ou exclusivo bit a bit
<<: Deslocamento para a esquerda
>>: Deslocamento para a direita
~: Negação bit a bit
6. Operadores de Identidade:

Os operadores de identidade são usados para verificar se duas variáveis se referem ao mesmo objeto na memória:

is: Verdadeiro se as variáveis se referem ao mesmo objeto
is not: Verdadeiro se as variáveis não se referem ao mesmo objeto
7. Operadores de Associação:

Os operadores de associação são usados para verificar se um valor está presente em uma sequência (lista, tupla, string, etc.):

in: Verdadeiro se o valor está presente na sequência
not in: Verdadeiro se o valor não está presente na sequência
8. Operador Ternário:

O operador ternário é uma forma concisa de escrever uma estrutura condicional if-else em uma única linha:

condição_verdadeira if condição else condição_falsa
"""

x = 10
y = 5

soma = x + y  # Operador aritmético (+)
print(soma)  # Saída: 15

maior = x > y  # Operador de comparação (>)
print(maior)  # Saída: True

resultado = x > 5 and y < 10  # Operadores lógicos (and)
print(resultado)  # Saída: True

x += 3  # Operador de atribuição (+=)
print(x)  # Saída: 13

lista = [1, 2, 3]
esta_presente = 2 in lista  # Operador de associação (in)
print(esta_presente)  # Saída: True

mensagem = "Parabéns!" if x > 10 else "Tente novamente."  # Operador ternário
print(mensagem)  # Saída: Parabéns!