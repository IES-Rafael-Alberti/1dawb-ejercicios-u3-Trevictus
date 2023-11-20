"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso."""

def creditos_asignaturas():
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

    for asignatura, credito in asignaturas.items():
        print("La asignatura",asignatura,"tiene", credito, "créditos.")

    print("El total de créditos de las asignaturas ees: ",sum(asignaturas.values()))

creditos_asignaturas()