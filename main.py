#Calculadora com while

while True:
    numero_1 = input('insira o numero ')
    numero_2 = input("insira o outro numero ")
    
    operador = input("o que deseja fazer? (+-/*) ")
    
    ##Validando numeros
    
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        
        
        print("tudo ok")
    except:
        print("numeros invalidos")
        continue
       
    ##Validando operador
    
    
    operadores_permitidos = '+-/*' 
    if len(operador) > 1:
        print('apenas um operador')
        continue
    
    if operador not in operadores_permitidos:
        print("Não esta nos operadores")
        continue
       
       
    if operador == "+":
        print(numero_1+numero_2)
    elif operador == "-":
        print(numero_1-numero_2)
    elif operador == "/":
        print(numero_1/numero_2)
    elif operador == "*":
        print(numero_1*numero_2)
    
          
        
    sair = input("quer sair?S/N ").upper().startswith('S')
    
    if sair:
        print("Saiu") 
        break
    