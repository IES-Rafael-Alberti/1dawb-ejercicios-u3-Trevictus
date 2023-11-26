

def producto_vectorial(v1: tuple, v2:tuple) -> tuple:
    cont = 0
    l3 = []
    while cont < len(v1):
        l3.append(v1[cont]* v2[cont])
        cont +=1
    
    return tuple(l3)



def main():
    v1 = (1, 2, 3)
    v2 = (2, 3, 4)


    v3 = producto_vectorial(v1, v2)

    print(v3)

if __name__ == "__main__":
    main()