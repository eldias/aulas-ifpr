primeira_palavra = input("Insira a primeira palavra: ")
segunda_palavra = input("Insira a segunda palavra: ")
terceira_palavra = input("Insira a terceira palavra: ")

if primeira_palavra < segunda_palavra and primeira_palavra < terceira_palavra:
    if segunda_palavra < terceira_palavra:
        print(primeira_palavra, segunda_palavra, terceira_palavra)
    else:
        print(primeira_palavra, terceira_palavra, segunda_palavra)
elif segunda_palavra < primeira_palavra and segunda_palavra < terceira_palavra:
    if primeira_palavra < terceira_palavra:
        print(segunda_palavra, primeira_palavra, terceira_palavra)
    else:
        print(segunda_palavra, terceira_palavra, primeira_palavra)
else:
    if terceira_palavra < segunda_palavra and terceira_palavra < primeira_palavra:
        print(terceira_palavra, primeira_palavra, segunda_palavra)
    else:
        print(terceira_palavra, segunda_palavra, primeira_palavra)