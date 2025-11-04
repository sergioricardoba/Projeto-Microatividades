# 1. Crie uma variável chamada texto e atribua a ela o valor ‘Olá, laço for.’;
# 2. Crie uma instrução for que itere sobre a variável texto atribuindo cada um de
# seus caracteres a uma variável chamada item;
# 3. Imprima, na tela, dentro do escopo do laço for, o valor da variável item precedido
# do texto ‘Caractere: ‘;
# 4. Crie, no mesmo script, uma nova instrução for que:
# Itere sobre um intervalo numérico entre 1 e 10 (dica: use a instrução range);
# range(1, 11) gera números de 1 até 10
# 5. Imprima, na tela, dentro do escopo do laço for, o valor de cada número no
# intervalo acima precedido do texto ‘Número do intervalo: ‘ ;
# Lembre-se de utilizar a instrução str para concatenar o valor inteiro com a string
# no momento de imprimir o valor pedido na tela.

texto = 'Olá, laço for.'

print('--- Primeiro Loop (Iterando sobre a string) ---')
for item in texto:
    print('Caractere: ' + item)
print('\n--- Segundo Loop (Iterando sobre o intervalo numérico) ---')
for numero in range(1, 11): 
    print('Número do intervalo: ' + str(numero))