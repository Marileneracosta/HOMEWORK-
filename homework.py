
entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

# TODO: Calcule o ICM da comunica��o dos Palat�r de Sauron e Saruman, com 2 casas decimais no espa�o #em branco abaixo:
soma = (diametro1 + diametro2)
resultado = distancia/soma

print (f"{resultado: 2.2f}")