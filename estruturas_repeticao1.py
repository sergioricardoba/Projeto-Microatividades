# 1. Crie uma variável chamada entrada_idade e atribua a ela o valor ‘’;
# 2. Crie uma instrução while que verifique se o valor atribuído à variável
# entrada_idade é diferente de 0 (como o valor inicial atribuído à variável é ‘’, isso
# a definiu como tipo string. Logo, a verificação no While deve ser feita com auxílio
# da instrução str );
# 3. No escopo da instrução while, atribua à variável entrada_idade um input de
# entrada de dados com o texto ‘Digite um número qualquer ou 0 para sair: ‘;
# 4. Imprima, na tela, o número digitado pelo usuário precedido do texto ‘Número digitado: ‘;
# A impressão deve ocorrer APENAS se o valor não for '0', para evitar a impressão final.

entrada_idade = ''

while entrada_idade != '0':
     entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
     if entrada_idade != '0':
        print(f'Número digitado: {entrada_idade}')
print('Saindo do programa.')