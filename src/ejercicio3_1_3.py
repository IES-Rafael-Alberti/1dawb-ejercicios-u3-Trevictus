"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario."""


def lista_asignaturas():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    nota = []

    for asignatura in asignaturas:
        notas  = float(input("¿Cuanto has sacado en "+asignatura+"?"))
        nota.append(notas)
        
    for i in range(len(asignaturas)):
        print(asignaturas[i],nota[i])


def main():
    lista_asignaturas()

if __name__ == "__main__":
    main()