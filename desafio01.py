n = int(input("Digite o número de escadas desejado: "))
a=n-1
for x in range (n):
    for y in range(n): 
        if y < a:
            print(' ', end='')
        else:
            print('*', end='')
    print()
    a-=1