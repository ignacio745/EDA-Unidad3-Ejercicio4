import csv

from ListaSecuencial import ListaSecuencial

from Designacion import Designacion



if __name__ == "__main__":
    archivo = open("estadistica-designacion-magistrados-federal-nacional-por-genero-20220323.csv")
    reader = csv.reader(archivo)
    unaLista = ListaSecuencial(400, Designacion)
    
    next(reader)

    for fila in reader:
        unaDesignacion = Designacion(fila[0], fila[1], fila[2], fila[3], fila[4], int(fila[5]), int(fila[6]))
        unaLista.insertar(unaDesignacion, unaLista.cantidad()+1)
    

    cargo = input("Ingrese un tipo de cargo: ")



    print("{0:^20}{1:^20}".format("Año", "Mujeres"))

    for i in range(1, unaLista.cantidad()+1):
        unaDesignacion:Designacion = unaLista.recuperar(i)
        if unaDesignacion.getCargoTipo().lower() == cargo.lower():
            print("{0:^20}{1:^20}".format(unaDesignacion.getAñoDesignacion(), unaDesignacion.getCantidadMujeres()))
    

    materia = input("Ingrese una materia: ")
    cargo = input("Ingrese un tipo de cargo: ")
    año = input("Ingrese un año: ")

    cantidad = unaLista.cantidad()

    i = 1
    
    unaDesignacion = unaLista.primer_elemento()
    while i <= cantidad and unaDesignacion.getMateria().lower() != materia and unaDesignacion.getCargoTipo().lower() != cargo.lower() and unaDesignacion.getAñoDesignacion() != año:
        i += 1
        unaDesignacion = unaLista.recuperar(i)
    
    if i > cantidad:
        print("No se encontro la designacion especificada")
    
    else:
        print("La cantidad de agentes designados en esa designacion fueron {0} ({1} varones y {2} mujeres)".format(unaDesignacion.getCantidadVarones()+unaDesignacion.getCantidadMujeres(), unaDesignacion.getCantidadVarones(), unaDesignacion.getCantidadMujeres()))
    