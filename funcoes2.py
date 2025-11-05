# Defina uma função chamada “loginUsuario”. Tal instrução receberá como
# parâmetro a variável perfil;
# No escopo da função, verifique se o valor do parâmetro perfil é igual a ‘admin’.
# Dica: utilize a instrução lower no momento de fazer a verificação;
# Caso o valor do parâmetro seja igual a ‘admin’, imprima na tela: ‘Bem-vindo, Administrador’.
# Do contrário, imprima: ‘Bem-vindo, Usuário’;
# Fora do escopo da função, faça a chamada da mesma passando diferentes valores como parâmetro.
# Primeira chamada: 'Admin'

def loginUsuario(perfil):
    if perfil.lower() == 'admin':
       print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')
loginUsuario('usuário')