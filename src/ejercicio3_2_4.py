"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes"""

def formato_fecha():
    meses = {1: "Enero",2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto",9:"Septiembre",10:"Octubre", 11:"Nobiembre", 12:"Diciembre"}

    formato = input("Introduce la fecha en formato dd/mm/aaaa: ")
    dia, mes, anio = formato.split("/")
    mes = meses[int(mes)]
    print(dia, mes, anio)


formato_fecha()