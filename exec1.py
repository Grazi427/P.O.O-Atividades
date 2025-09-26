import math

# FUNÇÃO PARA CALCULAR A DISTÂNCIA ENTRE OS PONTOS
def distancia(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

# FUNÇÃO PARA DEFINIR SE O TRIÂNGULO EXISTE/ONDE OS LADOS SÃO FORMADOS
def forma_triangulo(a,b,c):
    ab=distancia(a,b)
    bc=distancia(b,c)
    ca=distancia(c,a)
    return ab+bc>ca and ab+ca>bc and bc+ca>ab

# FUNÇÃO PARA DEFINIR SE É ISÓSCELES, ESCALENO OU EQUILATERO
def tipo_triangulo(a,b,c):
    ab=distancia(a,b)
    bc=distancia(b,c)
    ca=distancia(c,a)
    # TOLERANCIA DE CASAS DECIMAIS
    tol=1e-3
    if abs(ab-bc)<tol and abs(bc-ca)<tol:
        return "Equilátero"
    elif abs(ab-bc)<tol or abs(bc-ca)<tol or abs(ca-ab)<tol:
        return "Isósceles"
    else:
        return "Escaleno"

# FUNÇÃO PARA DEFINIR O TIPO DE QUADRILATERO
def tipo_quadrilatero(pontos):
    # ORDENA OS PONTOS PARA FACIITAR A VERIFICAÇÃO
    pontos = sorted(pontos, key=lambda p: (p[0], p[1]))
    a, b, c, d = pontos
    lados=[
        distancia(a,b),
        distancia(b,d),
        distancia(d,c),
        distancia(c,a)
    ]
    diag1=distancia(a,d)
    diag2=distancia(b,c)
    tol=1e-3

    lados_iguais=all(abs(l-lados[0])<tol for l in lados)
    ang_90=abs(diag1-diag2)<tol

    if lados_iguais and ang_90:
        return "O quadrilátero é do tipo: Quadrado"
    elif abs(lados[0]-lados[2])<tol and abs(lados[1]-lados[3])<tol and ang_90:
        return "O quadrilátero é do tipo: Retângulo"
    else:
        return "Outro tipo de quadrilátero, não é um quadrado nem retângulo"

# ESCOLHA SE SERÁ TRIÂNGULOS OU QUADRILATEROS
print("Você quer verificar 3 ou 4 pontos?")
esc=input("Digite 3 para triângulo ou 4 para quadrilátero: ")

if esc=="3":
    # EXEMPLOS DE COORDENADAS CASO O USUARIO QUEIRA
    ex=input('Deseja um exemplo de coordenadas de um triângulo? (s/n) ').lower()
    if ex=='s':
        t=input('Você deseja exemplos de qual tipo de triângulo? (equilátero, escaleno, isósceles) ')
        
        if t=='equilátero':
            print('Aqui estão dois exemplos de coordenadas para três pontos que formam um triângulo equilátero: \n')
            print('Exemplo 1')
            print('Ponto A: (0, 0)')
            print('Ponto B: (2, 0)')
            print('Ponto C: (1, 1.732)\n')

            print('Exemplo 2')
            print('Ponto A: (1,1)')
            print('Ponto B: (3,1)')
            print('Ponto C: (2, 2.732)\n')

        elif t=='escaleno':
            print('Aqui estão dois exemplos de coordenadas para três pontos que formam um triângulo escaleno:\n')
            print('Exemplo 1')
            print('Ponto A: (0, 0)')
            print('Ponto B: (3, 0)')
            print('Ponto C: (2, 2)\n')

            print('Exemplo 2')
            print('Ponto A: (0,0)')
            print('Ponto B: (4,1)')
            print('Ponto C: (2, 5)\n')

        elif t=='isósceles':
            print('Aqui estão dois exemplos de coordenadas para três pontos que formam um triângulo isósceles:\n')
            print('Exemplo 1')
            print('Ponto A: (0, 0)')
            print('Ponto B: (2, 0)')
            print('Ponto C: (1, 2)\n')

            print('Exemplo 2')
            print('Ponto A: (0,0)')
            print('Ponto B: (4,0)')
            print('Ponto C: (2, 3)\n')

        else:
            print('Opção inválida. Por favor, digite uma das opções sujeridas')
    else:
        print('OK!')



    print("\nDigite as coordenadas dos três pontos:")
    x1,y1=map(float, input("Digite as cordenadas do ponto A (x y): ").split())
    x2,y2=map(float, input("Digite as cordenadas do ponto B (x y): ").split())
    x3,y3=map(float, input("Digite as cordenadas do ponto C (x y): ").split())
    a=(x1,y1)
    b=(x2,y2)
    c=(x3,y3)
    if forma_triangulo(a,b,c):
        print("\nOs pontos formam um triângulo.\n")
        print("O triângulo é do tipo: ",tipo_triangulo(a,b,c))
    else:
        print("Os pontos não formam um triângulo.")

elif esc=="4":
    print("\nDigite as coordenadas dos quatro pontos:")

    pontos = []
    for i in range(4):
        x, y = map(float, input(f"Digite as cordenadas do ponto {chr(65+i)} (x y): ").split())
        pontos.append((x, y))

    tipo=tipo_quadrilatero(pontos)
    print('\n',tipo)

else:
    print("Opção inválida. Por favor, digite 3 ou 4.")
