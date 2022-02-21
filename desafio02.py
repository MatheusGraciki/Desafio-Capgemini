def password():
    global senha
    senha = input('\nDigite sua senha: ')
#verifica se não há espaços em branco e se atingiu o número minimo de caracteres     
def verify_caracter():
    global falta
    list(senha)
    cont = 0
    min = 6
    for i in range(0, len(senha)):
        
        if senha[i]== " ":
            print('Sua senha não pode conter espaços em branco.\nTente novamente!\n')
            password()
        else:
           
            cont+= 1 
   
    if cont < min:
        falta = min 
        return True
    else:
        return False
#verifica se existe ao menos 1 numero. any()verifica se ao menos 1 dos elementos é verdadeiro  
def verify_number():
    
    if not any(i.isdigit() for i in senha):
        return True
    else:
        return False
#verifica se existe ao menos 1 letra minuscul  
def verify_lowercase():
    
    if not any(i.islower() for i in senha):
        return True
    else:
        return False
  #verifica se existe ao menos 1 letra maiuscula
def verify_uppercase():
  
    if not any(i.isupper() for i in senha):
        return True
    else:
        return False

def verify_symbol():    
    # verifica se existe ao menos 1 dos caracteres abaixo, na senha 
    simbol = ['!','@','#','$','%','^','&','*','(',')','-','+']
    if not set(simbol) & set(senha):
        return True
    else:
        return False

def Desafio2():
    while (verify_caracter() or verify_number() or verify_lowercase() or verify_uppercase() or verify_symbol()) == True:

        print("\nSua senha deve conter no mínimo:")
             
        if verify_caracter() == True:
            print("6 caracteres")
        if verify_number() == True:
            print('1 número.')
        if verify_lowercase() == True:
            print('1 letra minúscula.')
        if verify_uppercase() == True:
            print('1 letra maiúscula.')
        if verify_symbol() == True:
            print('1 dos caracteres [!@#$%^&*()-+].')

        password()
   
    print('\nSua senha foi registrada sucesso!')


password()
Desafio2()